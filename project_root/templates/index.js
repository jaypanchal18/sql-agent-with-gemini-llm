<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Query Interface</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Natural Language Query Interface</h1>
        <form id="queryForm" class="mt-4">
            <div class="form-group">
                <label for="queryInput">Enter your query:</label>
                <input type="text" class="form-control" id="queryInput" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <div id="response" class="mt-4"></div>
    </div>

    <script>
        $(document).ready(function() {
            $('#queryForm').on('submit', function(event) {
                event.preventDefault();
                const query = $('#queryInput').val();
                $.ajax({
                    url: '/api/query',
                    method: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ query: query }),
                    success: function(data) {
                        $('#response').html('<h4>Response:</h4><p>' + data.response + '</p>');
                    },
                    error: function(xhr, status, error) {
                        $('#response').html('<h4>Error:</h4><p>' + xhr.responseText + '</p>');
                    }
                });
            });
        });
    </script>
</body>
</html>