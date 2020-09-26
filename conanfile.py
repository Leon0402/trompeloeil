#
# Trompeloeil C++ mocking framework
#
# Copyright Bjorn Fahller 2017-2019
#
#  Use, modification and distribution is subject to the
#  Boost Software License, Version 1.0. (See accompanying
#  file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
#
# Project home: https://github.com/rollbear/trompeloeil
#

from conans import ConanFile, CMake


class TrompeloelConan(ConanFile):
    name = "trompeloeil"
    version = "v38"
    license = "Boost Software License - Version 1.0 - August 17th, 2003"
    url = "https://github.com/rollbear/trompeloeil.git"
    description = "Header only C++14 mocking framework"
    exports_sources = "include/*", "LICENSE*.txt", "CMakeLists.txt", "*.cmake", "docs/*"
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def package_id(self):
        self.info.header_only()

    def package(self):
        cmake = CMake(self)
        cmake.definitions["TROMPELOEIL_INSTALL_DOCS"] = "OFF"
        cmake.configure(build_folder='build')
        cmake.install()
        self.copy("LICENSE*.txt", dst="licenses")
