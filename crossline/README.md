# Crossline

A daily geography puzzle. Two cities are joined by the shortest route over the
globe (a great circle, the way a plane flies). Find every country the line
passes through, by tapping the map or typing names. The cities' own countries
are given. Misses are counted; hints reveal the next country along the route.

- `index.html` is the game. It draws the map with d3-geo and topojson-client,
  loaded from jsDelivr.
- `world.js` holds the country shapes (world-atlas 2.0.2, Natural Earth
  1:110m, public domain). Very small countries such as Andorra or Singapore
  aren't on this map, so they're never part of an answer either.
- `data.js` holds the cities, country names and aliases, and 365 days of
  routes starting 2026-11-07, then loops.
- `places.mjs` is where cities, display names and aliases are edited.
- `generate.mjs` rebuilds `data.js` and `world.js`:
  `npm install && node generate.mjs`.

A route is only used when the answer is clear-cut. Every country must hold at
least 40 km of the line, and shifting the line about 25 km in any direction
must not change which countries it crosses, so nothing is merely clipped or
narrowly missed.
