def test_problem_flow(client):
    from scripts.seed_content import seed

    seed()
    courses = client.get("/api/courses").json()
    assert courses[0]["name"] == "Python 基础"
    problems = client.get("/api/problems").json()
    assert len(problems) >= 8
    p = client.get("/api/problems/1").json()
    assert p["code"] == "PY-BAS-001"
    r = client.post("/api/submissions", json={"problem_id": 1, "code": "print('wrong')"})
    assert r.status_code == 200
    assert r.json()["status"] == "FAILED"
    r = client.post("/api/submissions", json={"problem_id": 1, "code": "print('Hello, Python!')"})
    assert r.json()["status"] == "PASSED"
    assert client.get("/api/progress").json()["completed_problems"] == 1
