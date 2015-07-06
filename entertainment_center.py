import page_constructor
import media


"""Using Python 2.7, Execute/Run this Python file: entertainment_center.py \
and a browser window will open and render the top 10 Nicolas Cage movies. \
Instances below represent: title, description, movie poster image, and a \
youtube.com trailer that will display in a popup modal when movie \
image is clicked."""


bangkok_dangerous = media.Movie(
    "Bangkok Dangerous",
    2008,
    "As a hired assassin, Joe (Nicolas Cage) is the best in the business, but \
    the years of stone-cold murder have taken their toll. Joe's plan to make \
    this current assignment in Bangkok his last takes a wild turn when he \
    violates one of...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/Bangkok_dangerous_2008_poster.jpg/220px-Bangkok_dangerous_2008_poster.jpg",  # noqa
    "https://youtu.be/e_b2QVAVRpc",
    100)

season_witch = media.Movie(
    "Season Of The Witch",
    2011,
    "In Villach in the 13th century, three women are accused of witchcraft by \
    a priest (Nick Sidi). While one claims to be a witch out of persuasion \
    from the church, one doesn't deny it and curses the priest...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Season_of_the_Witch.jpg/220px-Season_of_the_Witch.jpg",  # noqa
    "https://youtu.be/PE6QUf1b-Xw",
    98)

snake_eyes = media.Movie(
    "Snake Eyes",
    1998,
    "Cage is an Atlantic City cop who, along with an arena full of spectators \
    at a championship prize-fight, is eyewitness to a political \
    assassination. Determined to quickly solve the crime, he immediately \
    launches an intensive investigation...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/SnakeEyesPoster.jpg/220px-SnakeEyesPoster.jpg",  # noqa
    "https://youtu.be/xzewDVXmSII",
    98)

zandalee = media.Movie(
    "Zandalee",
    1991,
    "Johnny, an artist painter by trade, has been working for Thierry's \
    business to help support his paintings. His only religion is \
    self-gratification. Johnny also sells and mules cocaine for a local drug \
    dealer as another source of income for...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Zandalee.jpg/220px-Zandalee.jpg",  # noqa
    "https://youtu.be/qYsyABPvtU0",
    104)

deadfall = media.Movie(
    "Deadfall",
    1993,
    "Lou is working on a con worth more than $2 million in diamonds. Eddie \
    (Nicolas Cage), Lou's right-hand man, sees Joe as a serious threat, and \
    a rival for his girlfriend - the sexy Diane (Sarah Trigger). Diane \
    seduces Joe into the love...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Deadfall-movie.jpg/220px-Deadfall-movie.jpg",  # noqa
    "https://youtu.be/E1kbITvaV7Y",
    98)

boy_in_blue = media.Movie(
    "The Boy In Blue",
    1986,
    "A wild, uncontrollable youth, Ned Hanlan is adopted by a gambler named \
    Bill, who promotes the boy on the sculling circuit for his own monetary \
    gain. A businessman named Knox assumes control of Hanlan's career, but \
    when Ned discovers just...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Theboyinblue.jpg/220px-Theboyinblue.jpg",  # noqa
    "https://youtu.be/frHmNfqdlnE",
    93)

fire_birds = media.Movie(
    "Fire Birds",
    1990,
    "A joint task force operation between the Drug Enforcement Administration \
    and the U.S. Army has been formed to dismantle one of the largest drug \
    cartels operating in South America. Multiple attempts to assault \
    the cartel's...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Firebirdsposter.jpg/220px-Firebirdsposter.jpg",  # noqa
    "https://youtu.be/cuZaAOtQfp8",
    87)

guarding_tess = media.Movie(
    "Guarding Tess",
    1994,
    "Doug Chesnic is a Secret Service agent who takes great pride in his \
    job, performing his duties with the utmost professionalism. His \
    assignment for the last three years has been a severe test of his \
    patience. Doug is in charge of a team that has to meet the president's \
    time line for...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Guarding_Tess_1994.jpg/220px-Guarding_Tess_1994.jpg",  # noqa
    "https://youtu.be/pSIa0ofR-Bg",
    95)

face_off = media.Movie(
    "Face/Off",
    1997,
    "FBI Special Agent Sean Archer has a personal vendetta against civil \
    freelance terrorist Castor Troy who six years earlier killed Archer's \
    son Michael while trying to assassinate Archer. Archer lays an ambush to \
    capture Castor and his younger...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/FaceOff_%281997_film%29_poster.jpg/220px-FaceOff_%281997_film%29_poster.jpg",  # noqa
    "https://youtu.be/3zebJ_NoduE",
    139)

con_air = media.Movie(
    "Con Air",
    1997,
    "Former Army Ranger Cameron Poe is sentenced to prison for manslaughter \
    for using excessive force on a drunk man while trying to protect his \
    pregnant wife Tricia. Poe is paroled eight years later, and is to be \
    released after being flown to Alabama...",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Conairinternational.jpg/220px-Conairinternational.jpg",  # noqa
    "https://youtu.be/fWq-S1_1vnc",
    115)

movies = [bangkok_dangerous, season_witch, snake_eyes, zandalee, deadfall,
          boy_in_blue, fire_birds, guarding_tess, face_off, con_air]
page_constructor.open_movies_page(movies)
