import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P1 Movie Trailer Website Assignment // William Garrow</title>

    <!-- Bootstrap 3 -->
    <!-- <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css"> -->
    <!-- <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css"> -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <!-- LOCAL Bootstrap CSS -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css" rel="stylesheet">

    <!-- Google Fonts -->
    <link rel="stylesheet" href='http://fonts.googleapis.com/css?family=Roboto:400,100,300,700,400italic,700italic' rel='stylesheet' type='text/css'>

    <!-- Fasten Your SEAT BELT!!!  -->
    <link rel="stylesheet" href="assets/css/animate.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/prettyPhoto.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css" rel="stylesheet">
    <!--[if lt IE 9]><script src="assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script rel="stylesheet" src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script rel="stylesheet" src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->

<style type="text/css" media="screen">
        body {
            color: #2c3e50;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile h3 {
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            color: #2c3e50;
            cursor: pointer;
        }
        .movie-tile h3 {
            font-size: 18px;
        }
        .movie-tile p {
            font-size: 11px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="http://williamgarrow.com">P1 Movie Trailer Website Assignment // William Garrow</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Start Features ================================================== -->
        <section id="features" class="section">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <!-- Title -->
                        <div class="overview animate" data-animate="flipInX">
                            <h1><strong>Udacity's Assignment.</strong> My execution.</h1> <h3 style="text-transform:lowercase;">(Sort of like Python On Front-End Steroids).</h3>
                            <p class="lead"><strong>Project Description.</strong> In this project you will build a Movie Trailer Website where users can see your favorite movies and watch the trailers. You'll be writing server side code to store a list of movie titles, box art, poster images, and movie trailer URLs. The data will then be expressed on the web page and allow users to review the movies and watch the trailers. (Here's a hint: The data for the movies will be stored using Classes!)</p>
                        </div>
                        <div class="row">
                            <div class="col-md-8"></div>
                            <div class="col-md-4">
                                <blockquote>
                                <p>Sometimes people think I'm wearing a wig when I'm not wearing a wig, and then sometimes they think I'm not wearing a wig when I am wearing a wig.<br />  -- Nicolas Cage</p>
                                </blockquote>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================================================
        End Features -->

        <!-- Start Movie Gallery ================================================== -->
        <section id="gallery" class="section">
            <div class="container">
                <div class="row">
                    <div class="col-md-12 col-sm-12">
                        <div class="overview animate" data-animate="flipInY">
                            <h2><strong>What could be better than Nickelback and Coca-Cola you ask?</strong><br /><em>That Funky little monkey Coca-Cola rollercoaster</em> Nick Cage.</h2>
                            <p class="lead">Nicolas Cage is arguably either the worst or the best actor depending on who you ask. Here in one glorious place on the interwebs are the top 10 of either the greatest or the most terrible 'Cagey' flicks of all time. Results are curated based on the film, the acting, but more importantly the Nic's hairdo.</p>
                                </div>
                    </div>
                    <div class="row">
                          {movie_tiles}
                    </div>

                </div>
            </div>
        </section>

        <!-- ==================================================
        End Movie Gallery  -->

        <!-- Bootstrap LOCAL JavaScript ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="assets/js/jquery-1.10.2.min.js"></script>
        <script src="assets/js/bootstrap.js"></script>
        <script src="assets/js/waypoints.min.js"></script>
        <script src="assets/js/jquery.scrollto.min.js"></script>
        <script src="assets/js/jquery.localscroll.min.js"></script>
        <script src="assets/js/scripts.js"></script>

  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-3 col-sm-4 col-xs-12 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}">
    <h3>{movie_title} ({movie_year})</h3>
    <p>Description: {movie_storyline}.<br />Running Time: {movie_duration} minutes.</p>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            movie_duration=movie.duration,
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible