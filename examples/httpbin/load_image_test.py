# NOTE: Generated By HttpRunner v3.1.4
# FROM: load_image.yml


from rrtv_httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoadImage(HttpRunner):

    config = Config("load images").base_url("${get_httpbin_server()}")

    teststeps = [
        Step(
            RunRequest("get png image")
            .get("/image/png")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("get jpeg image")
            .get("/image/jpeg")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("get webp image")
            .get("/image/webp")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("get svg image")
            .get("/image/svg")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoadImage().test_start()
