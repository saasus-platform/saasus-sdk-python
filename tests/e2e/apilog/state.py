"""ApiLog E2E test state management.

ApiLogは参照系APIのみのため、クリーンアップ対象のリソースはありません。
既存のbilling/pricingと同じStateManagerインターフェースを提供します。
"""


class StateManager:
    """State管理とクリーンアップを提供するマネージャー"""

    @staticmethod
    def cleanup_all_resources() -> None:
        print("\n🧹 Cleaning up apilog resources... (no-op / read-only API)")

    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()
