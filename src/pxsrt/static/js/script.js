$(document).ready(function () {
// Sidebar Toggle
    $('#sidebarCollapse').on('click', function () {
        $('.sidenav').toggleClass('active');
    });

// Toolbar Upper
    $('#upper').on('click', function() {
      if ($(this).attr('value') == 'False') {
        $(this).attr('value', 'True');
      } else {
        $(this).attr('value', 'False');
      };
    });

// Toolbar Reverse
    $('#reverse').on('click', function() {
      if ($(this).attr('value') == 'False') {
        $(this).attr('value', 'True');
      } else {
        $(this).attr('value', 'False');
      };
    });

// Preview Button
    $('#previewButton').on('click', function() {
      var blurValue = 'blur(10px)';
      $('#imgpg-img').css({
         'filter'         : blurValue,
         '-webkit-filter' : blurValue,
         '-moz-filter'    : blurValue,
         '-o-filter'      : blurValue,
         '-ms-filter'     : blurValue
      });
      var image_id = $(this).attr('image_id');
      var mode = $('#mode').val();
      var threshold = $('#threshold').val()
      var direction = $('input[name="direction"]:checked').val();
      var upper = $('#upper').attr('value');
      var reverse = $('#reverse').val();

      req = $.ajax({
        url: '/image/preview',
        type: 'POST',
        data: { image_id : image_id, mode : mode, threshold : threshold, direction : direction, upper : upper, reverse : reverse }
      });

      req.done(function(data) {
        $('#imgpg-img').attr('src', '/static/' + data.path + data.filename).css({
           'filter'         : 'blur(0px)',
           '-webkit-filter' : 'blur(0px)',
           '-moz-filter'    : 'blur(0px)',
           '-o-filter'      : 'blur(0px)',
           '-ms-filter'     : 'blur(0px)'
         });
      });
    });
// Sort Button
    $('#sortButton').on('click', function() {
      var blurValue = 'blur(10px)';
      $('#imgpg-img').css({
         'filter'         : blurValue,
         '-webkit-filter' : blurValue,
         '-moz-filter'    : blurValue,
         '-o-filter'      : blurValue,
         '-ms-filter'     : blurValue
      });
      var image_id = $(this).attr('image_id');
      var mode = $('#mode').val();
      var threshold = $('#threshold').val()
      var direction = $('input[name="direction"]:checked').val();
      var upper = $('#upper').attr('value');
      var reverse = $('#reverse').val();

      req = $.ajax({
        url: '/image/sort',
        type: 'POST',
        data: { image_id : image_id, mode : mode, threshold : threshold, direction : direction, upper : upper, reverse : reverse }
      });

      req.done(function(data) {
        $('#imgpg-img').attr('src', '/static/' + data.path + data.filename).css({
           'filter'         : 'blur(0px)',
           '-webkit-filter' : 'blur(0px)',
           '-moz-filter'    : 'blur(0px)',
           '-o-filter'      : 'blur(0px)',
           '-ms-filter'     : 'blur(0px)'
         });
      });
    });
// Refresh Button
    $('#refreshButton').on('click', function() {
      var image_id = $(this).attr('image_id');

      req = $.ajax({
        url: '/image/refresh',
        type: 'POST',
        data: { image_id : image_id }
      });

      req.done(function(data) {
        $('#imgpg-img').attr('src', '/static/' + data.path + data.filename);
      });
    });

});
