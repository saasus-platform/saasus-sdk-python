"""
データモデル定義

E2Eテストフレームワークで使用するデータモデルを定義します。
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Union


@dataclass
class Step:
    """
    テストステップ
    
    ストーリー内の個別のAPI呼び出しと検証を表します。
    """
    method_name: str
    params: Union[Dict[str, Any], Callable[[Dict[str, Any]], Dict[str, Any]]]
    expected_status: Optional[int] = None
    validation_func: Optional[Callable[[Any], bool]] = None
    description: str = ""
    store_as: Optional[str] = None
    skip_on_dry_run: bool = False
    skip: bool = False
    skip_reason: Optional[str] = None
    allow_failure: bool = False  # Trueの場合、失敗してもストーリーを続行
    
    def __post_init__(self):
        """バリデーション"""
        if not self.method_name:
            raise ValueError("method_nameは必須です")
        if self.params is None:
            raise ValueError("paramsは必須です")


@dataclass
class Story:
    """
    テストストーリー
    
    一連の関連するAPIコールをまとめたテストシナリオを表します。
    """
    name: str
    description: str
    module: str
    setup: Optional[List[Step]] = None
    steps: List[Step] = field(default_factory=list)
    cleanup: Optional[List[Step]] = None
    tags: List[str] = field(default_factory=list)
    timeout: Optional[int] = None
    
    def __post_init__(self):
        """バリデーション"""
        if not self.name:
            raise ValueError("nameは必須です")
        if not self.module:
            raise ValueError("moduleは必須です")
        if not self.steps:
            raise ValueError("stepsは必須です（少なくとも1つのステップが必要）")


@dataclass
class StepResult:
    """
    ステップ実行結果
    
    個別のステップの実行結果を保持します。
    """
    step: Step
    success: bool
    executed_method_name: Optional[str] = None
    response: Optional[Any] = None
    status_code: Optional[int] = None
    error: Optional[Exception] = None
    execution_time: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    resolved_params: Optional[Dict[str, Any]] = None  # 実際に使用されたパラメータ


@dataclass
class StoryResult:
    """
    ストーリー実行結果
    
    ストーリー全体の実行結果を保持します。
    """
    story: Story
    success: bool
    step_results: List[StepResult] = field(default_factory=list)
    setup_results: List[StepResult] = field(default_factory=list)
    cleanup_results: List[StepResult] = field(default_factory=list)
    execution_time: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
