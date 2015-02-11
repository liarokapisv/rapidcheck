#include "rapidcheck/Assertions.h"

namespace rc {
namespace detail {

std::string makeDescriptionMessage(const std::string file,
                                   int line,
                                   const std::string &description)
{
    return
        file + ":" + std::to_string(line) + "\n" +
        description;
}

std::string makeExpressionMessage(const std::string file,
                                  int line,
                                  const std::string &expression,
                                  const std::string &expansion)
{
    return
        file + ":" + std::to_string(line) + "\n" +
        expression + "\n"
        "\n"
        "Expands to:\n" +
        expansion;
}

} // namespace detail
} // namespace rc
