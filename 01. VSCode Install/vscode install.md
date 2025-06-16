# VSCode Installation Instructions

## Installation Steps

1. https://vscode.download.prss.microsoft.com/dbazure/download/stable/dfaf44141ea9deb3b4096f7cd6d24e00c147a4b1/code_1.101.0-1749655245_amd64.deb
2. Install the .deb package
    ```bash
    sudo apt install ./*.deb
    ```
3. Extensions to install:
    - Python
    - TODO+
    - autoDocstring
    - Better Comments
    - Jupyter
4. Settings
    - Theme -> Solarized Dark
    - Trim trailing whitespace
    - Auto save
    - Move parts of GUI around
5. First python script
    ```python
    #!/usr/bin/python3


    def devide(a: int, b: float) -> float:
        return a / b


    def main() -> None:
        print("Hello, World!")
        print(devide(1, 2.0))


    if __name__ == "__main__":
        main()

    ```
6. Change python interpreter
7. Run the script
8. Debug the script (F5)
    - Set breakpoints
        - Normal breakpoint
        - Conditional breakpoint
    - Start debugging
    - Show diffrent tabs
        - Variables
            - Local variables
            - Global variables
        - Watch
        - Call Stack
        - Breakpoints
            - Raise exception
            - Uncaught exceptions
            - User Uncaught exceptions
    - Hover variables to see their values
    - Show when a exception is raised
    - Toolbar
        - Continue
        - Step Over (Dont know)
        - Step Into
        - Step Out (Dont know)
        - Restart
        - Stop
    - Configure launch.json
9. autoDocstring Extension
    - Generate docstring on devide function (use while on line after function definition)
10. TODO+ Extension
    - Inline TODOs
    ```python
    def divide(a: float, b: float) -> float: # TODO: Test implementation
        return a / b
    ```
    - Create TODO file
    - Shortcuts
        - `Alt + Enter` -> Create new TODO
        - `Alt + S` -> TODO Started
        - `Alt + D` -> TODO Done
11. Better Comments Extension
    - Show different comment styles
    ```python
    # TODO
    # * Important
    # ! Deprecated
    # ? Question
    ```

## Code

```python
#!/usr/bin/python3


def devide(a: int, b: float) -> float: #TODO: Test implementation
    """_summary_

    Arguments:
        a -- _description_
        b -- _description_

    Returns:
        _description_
    """
    return a / b


def main() -> None:
    # TODO
    # * Important
    # ! Deprecated
    # ? Question
    print("Hello, World!")
    print(devide(1, 2.0))

if __name__ == "__main__":
    main()

```