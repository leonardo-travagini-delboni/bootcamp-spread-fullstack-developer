<!DOCTYPE html>
<html lang="pt-br">

    <!--- HEAD DA PAGINA -->
    <head>
        <title>Meu primeiro site em PHP!</title>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

        <!--- CSS da classe "linha" -->
        <style type="text/css">
            .linha{
                font-weight: bold;
                color: green;
                padding-left: 10px;
                line-height: 50px;
            }
        </style>
    </head>

    <!--- BODY DA PAGINA -->
    <body>
        <!--- FUNÇÃO DE IMPRIMIR LINHAS EM FOR COM PHP -->
        <?php
            for ($i = 0; $i < 10; $i++) {
                print("<span class=\"linha\">Linha número: " . $i . "</span><br>");
            }
        ?>
    </body>

    <!--- JAVASCRIPT DA PAGINA -->
    <script type="text/javascript">
        $(document).ready(function(){
            alert("WooHoo!");
        });
    </script>
</html>
