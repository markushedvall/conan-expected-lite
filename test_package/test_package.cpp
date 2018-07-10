#include <nonstd/expected.hpp>

using namespace nonstd;

auto get(bool error) -> expected<int, const char*> {
  if (error) {
    return make_unexpected("error");
  } else {
    return 42;
  }
}

int main() {
  auto expected = get(false);
  if (!expected.has_value()) {
    return 1;
  }
}
