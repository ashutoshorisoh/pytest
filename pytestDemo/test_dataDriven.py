import pytest

# ✅ Interview Question: What is the purpose of @pytest.mark.usefixtures?
# 👉 Answer: It ensures that the specified fixture (dataDrivenFixture) runs before any test in this class.
@pytest.mark.usefixtures("dataDrivenFixture")
class TestDataDriven:

    # ✅ Interview Question: Why is 'dataDrivenFixture' passed as a parameter?
    # 👉 Answer: Fixtures in pytest are injected as function arguments when running tests.
    # This allows the test function to use the data provided by the fixture.

    # ✅ Interview Question: When do we need to pass a fixture as a parameter?
    # 👉 Answer: We pass a fixture as a parameter **when we need access to the fixture’s return value**.
    # If the fixture is only used for setup/teardown purposes, @pytest.mark.usefixtures is enough.
    def test_data(self, dataDrivenFixture):
        print(dataDrivenFixture[0])  # ✅ Interview Question: What does this print?
        # 👉 Answer: It prints the first element of the data provided by the fixture.
