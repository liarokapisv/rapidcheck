from conans import ConanFile, CMake, tools


class RapidcheckConan(ConanFile):
    name = "rapidcheck"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "enable_rtti" : [True, False],
        "enable_all_integrations" : [True, False],
        "enable_catch_integration" : [True, False],
        "enable_gmock_integration" : [True, False],
        "enable_gtest_integration" : [True, False],
        "enable_boost_integration" : [True, False],
        "enable_boost_test_integration" : [True, False],
    }

    default_options = (
            "shared=False", 
            "enable_rtti=True",
            "enable_all_integrations=False",
            "enable_catch_integration=False",
            "enable_gmock_integration=False",
            "enable_gtest_integration=False",
            "enable_boost_integration=False",
            "enable_boost_test_integration=False"
    )

    exports_sources = "CMakeLists.txt", "include/*", "src/*", "extras/*"

    def configure_cmake(self):
        cmake = CMake(self)
        if self.options.enable_rtti:
            cmake.definitions["RC_ENABLE_RTTI"] = True
        if self.options.enable_all_integrations:
            cmake.definitions["RC_ENABLE_ALL_EXTRAS"] = True
        if self.options.enable_catch_integration:
            cmake.definitions["RC_ENABLE_CATCH"] = True
        if self.options.enable_gmock_integration:
            cmake.definitions["RC_ENABLE_GMOCK"] = True
        if self.options.enable_gtest_integration:
            cmake.definitions["RC_ENABLE_GTEST"] = True
        if self.options.enable_boost_integration:
            cmake.definitions["RC_ENABLE_BOOST"] = True
        if self.options.enable_boost_test_integration:
            cmake.definitions["RC_ENABLE_BOOST_TEST"] = True
        cmake.configure()
        return cmake


    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
