class Ball:
    def __init__(self, ball_id: str, radius: int, color: str) -> None:
        self.ball_id = ball_id
        self.radius = radius
        self.color = color

    def __repr__(self) -> str:
        return f"Ball(ball_id={self.ball_id}, radius={self.radius}, color={self.color})"
    
ball_basic = Ball("basic", 10, (255, 204, 255))

ball_library = {
    ball_basic.ball_id : ball_basic
}
