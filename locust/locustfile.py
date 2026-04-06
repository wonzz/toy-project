from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    # 각 요청 사이의 대기 시간 (1~3초 사이 랜덤)
    wait_time = between(1, 3)

    @task(3)  # 비중 3: 메인 페이지 접속
    def view_main(self):
        self.client.get("/")

    @task(1)  # 비중 1: 아이템 상세 페이지 접속
    def view_item(self):
        self.client.get("/items/1")

    @task(1)  # 비중 1: 일부러 404 에러 유도 (알람 테스트용)
    def view_error(self):
        self.client.get("/not-found-page")
