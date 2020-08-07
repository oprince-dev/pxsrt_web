$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('.sidenav').toggleClass('active');
    });

    $('#previewButton').on('click', function() {
      var image_id = $(this).attr('image_id');
      var mode = $('#mode').val();
      var threshold = $('#threshold').val()
      var direction = $('input[name="direction"]').val();
      var upper = $('#upper').val();
      var reverse = $('#reverse').val();

      req = $.ajax({
        url: '/image/preview',
        type: 'POST',
        data: { image_id : image_id, mode : mode, threshold : threshold, direction : direction }
      });

      req.done(function(data) {
        $('#imgpg-img').attr('src', '/static/' + data.path + data.filename);
      });
    });

    $('#sortButton').on('click', function() {
      var image_id = $(this).attr('image_id');
      var mode = $('#mode').val();
      var threshold = $('#threshold').val()
      var direction = $('input[name="direction"]').val();
      var upper = $('#upper').val();
      var reverse = $('#reverse').val();

      req = $.ajax({
        url: '/image/sort',
        type: 'POST',
        data: { image_id : image_id, mode : mode, threshold : threshold, direction : direction }
      });

      req.done(function(data) {
        $('#imgpg-img').attr('src', '/static/' + data.path + data.filename);
      });
    });

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
