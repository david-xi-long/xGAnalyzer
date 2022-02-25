<?php
 echo "Connected successfully";
?>

<html>
<head>
    <style>
        .container0 {
          width: calc((100% - 130px)/5.5*2.35);
          padding: 0px 20px;
          height: 100px;
          background-color: #80e6e6;
          border: 1px solid black;
          float: left;
          display: block;
          font-size: xx-large;
        }
        .container1 {
          width: calc((100% - 130px)/5.5);
          padding: 0px 20px;
          height: 100px;
          background-color: #b746eb;
          border: 1px solid black;
          float: left;
          display: block;
          font-size: medium;
        }
        .container2 {
          width: calc((100% - 130px)/5.5);
          padding: 0px 20px;
          height: 100px;
          background-color: #e33bcd;
          border: 1px solid black;
          float: left;
          display: block;
          font-size: medium;
        }
        .container3 {
          width: calc((100% - 130px)/5.5);
          padding: 0px 20px;
          height: 100px;
          background-color: #f0279f;
          border: 1px solid black;
          float: left;
          display: block;
          font-size: medium;
        }
        .container5 {
            padding-top: 25px;
            background-color: #0096FF;
            color: #0096FF;
            height: 700px;
        }
        .container6 {
            margin-left: 100px;
            margin-right: 80px;
            padding-top: 25px;
            position: relative;
            background-color: lightblue;
            color: whitesmoke;
            height: 600px;
        }
        h1 {
        position: relative;
        color: grey;
        }
        h2 {
            font-size: medium;
            color: lightgray;
        }
        .header{
            padding-left: 100px;
        }
        .header img {
            float: left;
            width: 250px;
            height: 150px;
        }
        Body {
            font-family: Calibri, Helvetica, sans-serif;
            background-color: darkblue;
        }
    </style>
</head>
<body>
    <div class="header">
    <img src="https://i.ibb.co/K7K5D49/xgGraph.png" alt="logo" />
    <h1>&ensp;xG Analyzer</h1>
    </div>
      <h2>&emsp; We analyze, you decide </h2>
    <br><br><br>
    <div class="container">
        <div class="container0"><br>&emsp;&emsp;  Welcome back {{ user }}</div>
        <div class="container1"><br><br>Predict a  match based on xG graph</div>
        <div class="container2"><br><br>Find game result based on xG graph</div>
        <div class="container3"><br><br>Generate xG graph for soccer match</div>
    </div>
    <br><br><br><br><br><br><br>
    <div>
        <div class="container5">
            <div class="container6">Light Blue</div>
        </div>
    </div>
</body>
</html>
