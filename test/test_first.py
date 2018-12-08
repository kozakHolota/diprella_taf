class TestFirst(object):
    def test_first(self):
        assert self.main_app.signup_button.is_displayed(), "Sign up button is not present on the main page"
        assert self.main_app.diprella_logo.is_displayed(), "Home button is not present on the main page"
        assert self.main_app.search_field.is_displayed(), "Search field is not present on the main page"
        assert self.main_app.login_link.is_displayed(), "Login link is not present on the main page"
        assert self.main_app.library_link.is_displayed(), "Library link is not present on the main page"
        assert self.main_app.description_header.is_displayed(), "Description Header is not present on the main page"
        assert self.main_app.description_text.is_displayed(), "Description Text is not present on the main page"
        self.main_app.signup_button.click()