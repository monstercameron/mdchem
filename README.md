# mdchem
MDC chemistry back end

description:
    Save data, fetch data, display data, manage data, See trends.

dependencies:
    see requierements.txt

routes:
    /           -   home page
    /login      -   login page
    /logout     -   logout page
    /register   -   register usage
    /admin      -   admin management page
    /database   -   charts page
    /students   -   student data viewer


API:
    /save       -   POST{uid, level_id, data} sending data
    /data
        ?type=  -   POST{admin_id, data=git[level_id, all_levels] } sending request for data
    /highscore  -   GET{name, score}