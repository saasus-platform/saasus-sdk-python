"""Pricing E2E test state management."""


class StateManager:
    """State管理とクリーンアップを提供するマネージャー"""

    @staticmethod
    def cleanup_all_resources() -> None:
        print("\n🧹 Cleaning up pricing resources...")

    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()
