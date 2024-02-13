Many different setups are possible. There is no _right_ way of setting up your environment. The following serves as self-documentation and example.

## [rgaudin](https://github.com/rgaudin)'s with Sublime Text

- macOS
- Python for each minor stable using [python.org packages](https://www.python.org/downloads/)
- [hatch](https://pypi.org/project/hatch/) installed globally
- [Sublime Text 4](https://www.sublimetext.com/) (proprietary)
  - [LSP](https://lsp.sublimetext.io/)
  - [LSP-ruff](https://packagecontrol.io/packages/LSP-ruff)
  - [LSP-pyright](https://github.com/sublimelsp/LSP-pyright)
  - [Debugger](https://github.com/daveleroy/SublimeDebugger)
  - [sublack](https://github.com/jgirardet/sublack)
  - [TOML](https://github.com/jasonwilliams/sublime_toml_highlighting)
  - [Trailing Spaces](https://github.com/SublimeText/TrailingSpaces)
  - _non-required but useful for openZIM projects_
  - [Vue Syntax Highlighting](https://github.com/vuejs/vue-syntax-highlight)
  - [Pretty YAML](https://github.com/aukaost/SublimePrettyYAML)
  - [LSP-json](https://github.com/sublimelsp/LSP-json)
  - [LSP-dockerfile](https://github.com/sublimelsp/LSP-dockerfile)
  - [JSON Reindent](https://github.com/ThomasKliszowski/json_reindent)
  - [Dockerfile Syntax Highlighting](https://github.com/asbjornenge/Docker.tmbundle)

```sh
# create (if missing) default env, installing dependencies
# also verifies default env's python version (use a matrix for default with a single value to set otherwise)
hatch run python -V

# make sure it's correct
hatch env show
hatch env find

# symlink hatch's default environment into `./.venv` (in project)
ln -s "$(hatch env find)" .venv
```

The key part is the symlink to `.venv` so that LSP-pyright and other tool can automatically find the environment and properly detect the installed dependencies.


## [benoit74](https://github.com/benoit74)'s with Visual Studio Code

- macOS
- [brew](https://brew.sh/)
- [pyenv](https://github.com/pyenv/pyenv) (installed with brew) 
- Python:
  - at least each supported and released minor versions (i.e. security + bugfix on https://devguide.python.org/versions/)
  - installed with `pyenv install x.y.z`
  - all supported and released minor versions are set in `/Users/<username>/.python-version` (i.e. available when looking for a version with python, python3, python3.x, ...)
- [hatch](https://pypi.org/project/hatch/) installed globally
- [Visual Studio Code](https://github.com/microsoft/vscode) with following extensions (more or less related to Python development)
  - Black Formater (Microsoft)
  - Dev Containers (Microsoft)
  - Docker (Microsoft)
  - Excalidraw (pomdtr)
  - Even Better TOML (tamasfe)
  - GitLens (GitKraken)
  - Jupyter (Microsoft)
  - Pylance (Microsoft)
  - Python (Microsoft)
  - Remote Development (Microsoft)
  - reStructuredText (LeXtudio Inc.)
  - Ruff (Astral Software)
  - Volar (Vue)
  - YAML (Red Hat)

Hatch is configured with an additional section in `config.toml` (configuration file is located in `~/Library/Application Support/hatch`, see https://hatch.pypa.io/latest/config/hatch/, correct file is shown by `hatch status` in any case).
```
[dirs.env]
virtual = ".hatch"
```

This additional Hatch config section ensures that all virtual environments (the only built-in environment in hatch is `virtual` - for now at least) are created in a `.hatch` subfolder inside the project folder ; it is mandatory so that Visual Studio Code will be able to find these dependencies.

On every project, create a local `.vscode/settings.json` to automatically format your code (adjust `typeCheckingMode` depending on your project):
``` json
{

    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
    },
    "python.analysis.typeCheckingMode": "basic",
}
```

When starting to work on a project, start a shell on default env + installing dependencies + start VSCode ; starting VSCode from inside the hatch shell ensures he will find automatically the proper Python version and dependencies

```sh
hatch shell
pip install '.[dev]'
code .
```