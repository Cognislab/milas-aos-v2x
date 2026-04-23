# MiLAS v2.x Minimal Implementation
# Cognis-lab / 枝成豆太
# ---------------------------------------------
# L1: Stability Layer
# L2: Generation Layer
# L3: Policy Layer
# ---------------------------------------------

class L1_Stability:
    """認知の安定性・再起動性を扱う層（最小モデル）"""
    def __init__(self):
        self.state = "stable"

    def stabilize(self):
        self.state = "stable"
        return "L1: 状態を安定化しました"

    def reset(self):
        self.state = "reset"
        return "L1: 認知状態をリセットしました"


class L2_Generation:
    """認知処理の生成エンジン（最小モデル）"""
    def generate(self, input_signal: str):
        return f"L2: 入力「{input_signal}」から認知処理を生成しました"


class L3_Policy:
    """方針・制御層（最小モデル）"""
    def decide(self, context: str):
        return f"L3: 文脈「{context}」に基づき方針を決定しました"


# ---------------------------------------------
# MiLAS AOS v2.x — Minimal OS
# ---------------------------------------------
class MiLAS:
    def __init__(self):
        self.l1 = L1_Stability()
        self.l2 = L2_Generation()
        self.l3 = L3_Policy()

    def run(self, context: str, signal: str):
        """MiLAS の3層を最小限で通すデモ関数"""
        s1 = self.l1.stabilize()
        s2 = self.l3.decide(context)
        s3 = self.l2.generate(signal)
        return [s1, s2, s3]


# ---------------------------------------------
# Example usage
# ---------------------------------------------
if __name__ == "__main__":
    milas = MiLAS()
    result = milas.run(context="対話", signal="こんにちは")
    for r in result:
        print(r)
