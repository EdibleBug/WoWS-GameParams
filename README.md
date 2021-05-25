# World of Warships GameParams to JSON
[![License](https://img.shields.io/github/license/EdibleBug/WoWS-GameParams)](./LICENSE)

## Legal Notice and License
I acknowledge and agree to the rights and Terms of Use (ToS) provided by [Wargaming.net (WG)](https://wargaming.com/). Any users wishing to use the code or WoWSFT must also acknowledge and agree to the rights and ToS underlined by WG. I am not held responsible for any issues or problems that may occur related to using WoWSFT and/or provided codes.

Any codes and materials created by me are under [MIT License](./LICENSE).

## Instruction
1. Use Python 3.
2. Legacy folder is outdated.
3. Extract GameParams.data into same folder.
    * OneFileToRuleThemAll.py
        * Extracts into a huge JSON file with everything included.
    * OneFileToSplitThemAll.py
        * Splits into many JSON files, with file name as key and value as content.
        * Example folder/file structure
          ```
          __ root
            |__ sub
               |__ 0
                  |__ Ability
                  |   |__ PCY001_CrashCrew.json
                  |   |__ ...
                  |__ Achievement
                  |   |__ PCH001_DoubleKill.json
                  |   |__ ...
                  |__ ...
          ```

Original codes from XeNTax forum, modified a while ago due to incompatibility with data.

[GameParams2Json](https://github.com/imkindaprogrammermyself/GameParams2Json) referenced when refactoring code.
