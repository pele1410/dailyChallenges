/// \brief Challenge to build up sums of words based on character values
///
/// Source:
/// https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
///
/// Challenge
/// Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of
/// lowercase letters, find the sum of the values of the letters in the string.
///
/// lettersum("") => 0
/// lettersum("a") => 1
/// lettersum("z") => 26
/// lettersum("cab") => 6
/// lettersum("excellent") => 100
/// lettersum("microspectrophotometries") => 317
/// Optional bonus challenges
/// Use the enable1 word list for the optional bonus challenges.
///
/// microspectrophotometries is the only word with a letter sum of 317. Find the only word with
/// a letter sum of 319.
///
/// How many words have an odd letter sum?
///
/// There are 1921 words with a letter sum of 100, making it the second most common letter sum.
/// What letter sum is most common, and how many words have it?
///
/// zyzzyva and biodegradabilities have the same letter sum as each other (151), and their
/// lengths differ by 11 letters. Find the other pair of words with the same letter sum whose
/// lengths differ by 11 letters.
///
/// cytotoxicity and unreservedness have the same letter sum as each other (188), and they have
/// no letters in common. Find a pair of words that have no letters in common, and that have
/// the same letter sum, which is larger than 188. (There are two such pairs, and one word
/// appears in both pairs.)
///
/// The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words.
/// Each word in the list has both a different number of letters, and a different letter sum.
/// The list is sorted both in descending order of word length, and ascending order of letter
/// sum. What's the longest such list you can find?

#include <QFile>

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

namespace
{

// Application Arguments
static std::string const ARG_SUM_ALL_WORDS{"-a"}; ///< Main Challenge
static std::string const ARG_WORD_WITH_SUM{"-w"}; ///< Bonus #1
static std::string const ARG_MAX_SUM{"-m"};       ///< Bonus #3

static QString const DICTIONARY_FILE = "words.txt"; ///< Dictionary File

static int const ASCII_OFFSET = 96; ///< Offset from ascii 'a' value to this challenge
}

std::vector<std::string> dictionary ()
{
        QFile dict (DICTIONARY_FILE);
        if (!dict.open (QIODevice::ReadOnly | QIODevice::Text))
        {
                std::cerr << "Error opening " << DICTIONARY_FILE.toStdString () << "\n";
                return {};
        }

        std::vector<std::string> words{};

        while (!dict.atEnd ())
        {
                QByteArray line = dict.readLine ();
                line.chop (1);
                words.emplace_back (line.toStdString ());
        }

        return words;
}

int letterValue (char const &letter_)
{
        return static_cast<int> (std::tolower (letter_)) - ASCII_OFFSET;
}

int wordSum (std::string const &word_)
{
        int sum = 0;
        for (auto letter : word_)
                sum += letterValue (letter);

        return sum;
}

void findWordsWithSum (int const desiredSum_)
{
        auto const dict = dictionary ();
        for (auto const &word : dict)
        {
                auto const sum = wordSum (word);

                if (sum == desiredSum_)
                        std::cout << "Word " << word << " has desired sum of " << desiredSum_
                                  << "\n";
        }
}
void findMaxSum ()
{
        std::map<int, int> allSums{};

        auto const dict = dictionary ();
        for (auto const &word : dict)
        {
                auto const sum = wordSum (word);
                allSums[sum]++;
        }

        std::set<int> maxSums{};
        int maxSum = -std::numeric_limits<int>::max ();

        for (auto sum : allSums)
        {
                std::cout << "Sum of " << sum.first << " has " << sum.second << " words\n";
                if (sum.second >= maxSum)
                {
                        maxSum = sum.second;
                        maxSums.insert (sum.first);
                }
        }

        for (auto const &sum : maxSums)
        {
                std::cout << "Sum of " << sum << " has the max sum of " << maxSum << "\n";
        }
}

void printAllSums ()
{
        auto const dict = dictionary ();
        for (auto const &word : dict)
        {
                auto const sum = wordSum (word);
                std::cout << "Word " << word << " has a sum of " << sum << "\n";
        }
}

void showHelp ()
{
        std::cerr << "sumWords [options]\n";
        std::cerr << "\t -a\n";
        std::cerr << "\t -w NUM\n";
        std::cerr << "\t -m\n";
}

int main (int argc_, char **argv_)
{
        if (argc_ < 2)
        {
                std::cerr << "Missing required argument\n";
                showHelp ();
                return 1;
        }

        if (argv_[1] == ARG_SUM_ALL_WORDS)
        {
                printAllSums ();
        }
        else if (argv_[1] == ARG_MAX_SUM)
        {
                findMaxSum ();
        }
        else if (argv_[1] == ARG_WORD_WITH_SUM)
        {
                if (argc_ < 3)
                {
                        std::cerr << "Missing required argument\n";
                        showHelp ();
                        return 1;
                }

                findWordsWithSum (atoi (argv_[2]));
        }

        return 0;
}
