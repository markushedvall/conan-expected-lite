from conans import ConanFile, CMake, tools
from conans.tools import download, unzip
import os

class ExpectedLiteConan(ConanFile):
    name = "expected-lite"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/markushedvall/conan-expected-lite"
    description = "Expected objects for C++11 and later (and later perhaps C++98)"
    sources_folder = "sources"
    no_copy_source = True

    def source(self):
        download("https://github.com/martinmoene/expected-lite/archive/v%s.zip" % self.version, "%s.zip" % self.sources_folder)
        unzip("%s.zip" % self.sources_folder)
        os.unlink("%s.zip" % self.sources_folder)
        os.rename("%s-%s" % (self.name, self.version), self.sources_folder)

    def package(self):
        self.copy(pattern="*.hpp", dst="include", src="%s/include" % self.sources_folder, keep_path=True)

    def package_id(self):
        self.info.header_only()
