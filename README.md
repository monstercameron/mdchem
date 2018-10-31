# mdchem
MDC chemistry back end

description:
    Save data, fetch data, display data, manage data, See trends.

&nbsp;

dependencies:
    see requierements.txt

&nbsp;

routes:
    /           -   home page
    /login      -   login page
    /logout     -   logout page
    /register   -   register usage
    /recover    -   recover bad password
    /admin      -   admin management page

&nbsp;

API:
    /save       -   POST   POST{uid, level_id, data} sending data
    /data
        ?type=  -   GET/POST   POST{admin_id, data=get[level_id, all_levels] } sending request for data
    /highscore  -   GET  GET{name, score}

&nbsp;