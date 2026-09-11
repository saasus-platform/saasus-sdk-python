"""ApiLog API snapshot tests.

JavaScriptのapilogs.snapshot.tsを参考にしたスナップショットテスト。
既存のpricing/billingのsnapshotテスト構成を踏襲しています。
"""

import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from testlib.runner import StoryRunner
from testlib.reporter import Reporter
from testlib.snapshot import SnapshotEngine, SnapshotConfig
from tests.e2e.apilog.stories import get_apilog_stories
from tests.e2e.apilog.state import StateManager


def get_snapshot_mode() -> str:
    return os.getenv("SNAPSHOT_MODE", "capture")


def apply_snapshot_mode(mode: str) -> None:
    enable_capture = mode in ["capture", "full"]
    enable_comparison = mode in ["compare", "full"]
    enable_reporting = mode in ["report", "full"]
    snapshot_enabled = enable_capture or enable_comparison or enable_reporting

    os.environ["SNAPSHOT_MODE"] = mode
    os.environ["SNAPSHOT_ENABLED"] = str(snapshot_enabled).lower()
    os.environ["SNAPSHOT_DIR"] = "tests/snapshots"
    os.environ["SNAPSHOT_SUCCESS_ONLY"] = "true"


def describe_mode(mode: str) -> str:
    descriptions = {
        "capture": "📸 Mode: Capture only",
        "compare": "🔍 Mode: Compare only",
        "report": "📄 Mode: Report only",
        "full": "🔄 Mode: Full (Capture + Compare + Report)",
    }
    return descriptions.get(mode, "📸 Mode: Capture only")


class TestApilogSnapshot:
    """ApiLog API snapshot tests."""

    @pytest.fixture(scope="class", autouse=True)
    def setup_snapshot_mode(self):
        mode = get_snapshot_mode()
        apply_snapshot_mode(mode)

        print("\n🚀 Starting SaaSus ApiLog API Snapshot Tests")
        print("=" * 80)
        print(describe_mode(mode))
        print("=" * 80)

        yield

        print("\n🧹 スナップショットテスト完了後のクリーンアップを実行中...")
        try:
            StateManager.cleanup_all_resources()
            print("✅ クリーンアップが完了しました")
        except Exception as e:
            print(f"⚠️ クリーンアップ中に警告: {e}")

    def test_all_stories_snapshot(self, test_config, test_logger, sdk_client, coverage_tracker):
        story_runner = StoryRunner(sdk_client, test_config, test_logger)
        stories = get_apilog_stories()

        snapshot_config = SnapshotConfig.from_env()
        snapshot_engine = SnapshotEngine(snapshot_config, test_logger)

        story_results = []
        try:
            for story in stories:
                test_logger.info(f"\n{'=' * 80}")
                test_logger.info(f"Story: {story.name}")
                test_logger.info(f"Description: {story.description}")
                test_logger.info(f"{'=' * 80}")

                result = story_runner.run_story(story)
                story_results.append(result)

                for step_result in result.step_results:
                    coverage_tracker.record(
                        module=story.module,
                        method_name=step_result.step.method_name,
                        success=step_result.success,
                    )

                if snapshot_config.capture_enabled and result.success:
                    snapshot_engine.capture(result, sdk_client)

                if snapshot_config.compare_enabled:
                    diff = snapshot_engine.compare(result, sdk_client)
                    if diff:
                        test_logger.warning(
                            f"Snapshot differences detected for story: {story.name}"
                        )

                if not result.success:
                    StateManager.handle_story_failure(Exception(f"Story failed: {story.name}"))
                    pytest.fail(f"Story '{story.name}' failed")

            coverage_report = coverage_tracker.get_coverage_report()
            reporter = Reporter(test_config)
            reporter.generate(
                story_results=story_results,
                coverage_report=coverage_report,
                snapshot_diffs=None,
            )

            print("\n📊 Snapshot execution finished successfully.")
            print("✅ All ApiLog API E2E snapshot tests completed!")

        except Exception as error:
            print(f"\n❌ スナップショットテスト実行中にエラーが発生しました: {error}")
            StateManager.handle_story_failure(error)
            raise
