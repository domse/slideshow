<!doctype html>
<head>
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
  <script src="/js/responsiveslides.min.js"></script>

</head>
<body>
  <script>
    $(function() {
      $(".rslides").responsiveSlides({maxwidth: 800});
    });
  </script>
  <style>
    .rslides {
      position: relative;
      list-style: none;
      overflow: hidden;
      width: 100%;
      padding: 0;
      margin: 0;
      }

    .rslides li {
      -webkit-backface-visibility: hidden;
      position: absolute;
      display: none;
      width: 100%;
      left: 0;
      top: 0;
      }

    .rslides li:first-child {
      position: relative;
      display: block;
      float: left;
      }

    .rslides img {
      display: block;
      height: auto;
      float: left;
      width: 100%;
      border: 0;
      }
  </style>
  <ul class="rslides">
  % for picture in picturelist:
    <li><img src="{{picture}}" alt=""></li>
  % end
  </ul>
</body>
