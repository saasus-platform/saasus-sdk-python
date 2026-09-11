"""
Auth module story definitions

Authモジュールのテストストーリーを定義します。
"""

from typing import List
import sys
from pathlib import Path

# testlibをインポートパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story


def get_auth_stories() -> List[Story]:
    """
    Authモジュールのストーリー定義
    
    Returns:
        List[Story]: ストーリーのリスト
    """
    # 全ストーリーをインポート
    from tests.e2e.auth.stories_full import get_all_auth_stories
    return get_all_auth_stories()



# pytest統合用のテスト関数
# この関数はpytest_generate_tests()によって各ストーリーでパラメータ化されます
def test_story(
    story: Story,
    module_name: str,
    story_runner,
    coverage_tracker,
    story_results,
    test_config,
    snapshot_engine,
    request
):
    """
    ストーリーを実行するテスト関数
    
    pytest_generate_tests()によって動的に生成されたパラメータを使用して、
    各ストーリーを実行します。この関数はconftest.pyで定義されている
    test_story関数と同じシグネチャを持つ必要があります。
    
    Args:
        story: 実行するストーリー
        module_name: モジュール名
        story_runner: ストーリーランナー
        coverage_tracker: カバレッジトラッカー
        story_results: ストーリー結果のリスト
        test_config: テスト設定
        snapshot_engine: スナップショットエンジン
        request: pytestリクエスト
    """
    # conftest.pyのtest_story関数を呼び出し
    from tests.e2e.conftest import test_story as conftest_test_story
    conftest_test_story(
        story,
        module_name,
        story_runner,
        coverage_tracker,
        story_results,
        test_config,
        snapshot_engine,
        request
    )
