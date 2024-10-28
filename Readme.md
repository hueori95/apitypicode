
//install json-server instead of run by docker
npm i json-server

//create a new db.json
npx json-server db.json
//open localhost:3000 to check the updated data

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt

run all test: pytest -v
or run each test: pytest -m idtestcase (pytest -m tcid01)
or run test: pytest apitest/tests/users/test_create_users.py
or right-click on apitest/tests/users/test_*.py (ex: right click at test_create_users.py)


pytest --alluredir=allure-results // run test to report by allure

//view report
allure serve allure-results
or: allure generate allure-results --clean -o allure-report //open index.html at the allure-report folder







