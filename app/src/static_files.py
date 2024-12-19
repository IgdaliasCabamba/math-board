HTML = """
<html lang="en">

<head>
  <meta charset="utf-8" />
  <title>MathBoard0x1</title>
  <style>
    :root {
      --main-bg-color: {
          {
          cssvar_background
        }
      }

      ;
      --scrollbar-bg-color:transparent;
      --scrollbar-thumb-bg-color:rgba(250, 250, 250, 0.4);
      --scrollbar-thumb-hover-bg-color:rgb(250, 250, 250, 0.8)
    }
  </style>
  <link rel="stylesheet" href="/static/mstyle.css" />
</head>

<body>

  <math-field id="math-field" virtual-keyboard-mode="on"></math-field>

  <script>
    const VIEW_BOARD_HEIGHT = '98vh';
    const EDIT_BOARD_HEIGHT = '60vh';

    const mathField = document.getElementById('math-field');
    mathField.style.height = VIEW_BOARD_HEIGHT;

    mathField.addEventListener("focusout", () => {
      mathVirtualKeyboard.hide()
      mathField.style.height = VIEW_BOARD_HEIGHT;
    });

    document.addEventListener("click", (event) => {
      if (mathVirtualKeyboard.visible && mathField.style.height == VIEW_BOARD_HEIGHT) {
          mathField.style.height = EDIT_BOARD_HEIGHT;
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      else if(!mathVirtualKeyboard.visible) {
        mathField.style.height = VIEW_BOARD_HEIGHT;
      }
    });

    setTimeout(() => { mathVirtualKeyboard.show(); }, 1000);

    function QtAPI_setValue(value){
      mathField.value = value;
      return mathField.value;
    }
    function QtAPI_getValue(){
      return mathField.value;
    }

  </script>

  <script src="/static/packages/mathlive.min.js"></script>

</body>

</html>
"""

CSS = """
body {
    overflow-x: hidden;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    background-color: #f0f0f0;
    height: 100vh;
}
math-field {
    width: 98vw;
    height: 95vh;
    border: 2px solid #000;
    border-radius: 4px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    margin-top: 10px;
}
"""