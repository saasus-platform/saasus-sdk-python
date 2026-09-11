"""機密情報マスキング機能

このモジュールは、スナップショットに含まれる機密情報を自動的にマスキングする機能を提供します。
"""

import re
from typing import Any, List, Optional, Pattern


class Masker:
    """機密情報をマスキングするクラス
    
    APIレスポンスやスナップショットデータから機密情報を検出し、
    安全な値に置き換えます。
    
    Attributes:
        MASK_VALUE: マスキング時に使用する置換文字列
        DEFAULT_PATTERNS: デフォルトでマスキングするキーのパターンリスト
        patterns: マスキング対象のパターンリスト
        compiled_patterns: コンパイル済みの正規表現パターンリスト
        masked_count: マスキングされた値の総数
    """
    
    MASK_VALUE = "***MASKED***"
    
    DEFAULT_PATTERNS = [
        r"api_key",
        r"secret",
        r"password",
        r"token",
        r"authorization",
        r"credential",
        r"auth",
        r"bearer",
        r"access_key",
        r"private_key",
        r"client_secret",
        r"saas_id",
        # 生のリクエスト/レスポンスボディには他APIの認証情報等が
        # 埋め込まれ得るため、フィールドごとマスクする（例: apilogのログ本文）
        r"request_body",
        r"response_body",
    ]
    
    def __init__(self, custom_patterns: Optional[List[str]] = None):
        """Maskerを初期化
        
        Args:
            custom_patterns: カスタムマスキングパターンのリスト（オプション）
        """
        self.patterns: List[str] = self.DEFAULT_PATTERNS.copy()
        if custom_patterns:
            self.patterns.extend(custom_patterns)
        
        # 正規表現をコンパイル（大文字小文字を区別しない）
        self.compiled_patterns: List[Pattern] = [
            re.compile(pattern, re.IGNORECASE) 
            for pattern in self.patterns
        ]
        
        self.masked_count: int = 0
    
    def mask(self, data: Any) -> Any:
        """データ内の機密情報をマスク
        
        Args:
            data: マスキング対象のデータ（dict、list、またはプリミティブ型）
        
        Returns:
            マスキング済みのデータ
        """
        self.masked_count = 0
        return self._mask_recursive(data)
    
    def _mask_recursive(self, data: Any) -> Any:
        """再帰的にマスキングを適用
        
        ネストされたdict、list、プリミティブ型を適切に処理します。
        
        Args:
            data: マスキング対象のデータ
        
        Returns:
            マスキング済みのデータ
        """
        if isinstance(data, dict):
            return {
                key: self._mask_value(key, value)
                for key, value in data.items()
            }
        elif isinstance(data, list):
            return [self._mask_recursive(item) for item in data]
        else:
            # プリミティブ型（str、int、float、bool、None）はそのまま返す
            return data
    
    def _mask_value(self, key: str, value: Any) -> Any:
        """キーがパターンにマッチする場合、値をマスク
        
        Args:
            key: チェック対象のキー名
            value: マスキング対象の値
        
        Returns:
            マスキング済みの値、またはネストされたオブジェクトの場合は再帰処理結果
        """
        # キーがマスキング対象で、値がプリミティブ型の場合のみマスク
        if self._should_mask(key) and not isinstance(value, (dict, list)):
            self.masked_count += 1
            return self.MASK_VALUE
        
        # ネストされたオブジェクトを再帰的に処理
        return self._mask_recursive(value)
    
    def _should_mask(self, key: str) -> bool:
        """キーがマスキング対象かチェック
        
        Args:
            key: チェック対象のキー名
        
        Returns:
            マスキング対象の場合True、それ以外はFalse
        """
        return any(pattern.search(key) for pattern in self.compiled_patterns)
    
    def get_masked_count(self) -> int:
        """マスキングされた値の数を取得
        
        Returns:
            最後のmask()呼び出しでマスキングされた値の総数
        """
        return self.masked_count
    
    def add_pattern(self, pattern: str) -> None:
        """カスタムマスキングパターンを追加
        
        Args:
            pattern: 追加する正規表現パターン
        """
        self.patterns.append(pattern)
        self.compiled_patterns.append(re.compile(pattern, re.IGNORECASE))
    
    def reset_count(self) -> None:
        """マスキングカウンターをリセット"""
        self.masked_count = 0
