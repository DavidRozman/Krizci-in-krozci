% import model

    <h1> Križci in Krožci </h1>

    <h2> Polja na voljo: {{igra.prazna_polja() }} </h2>

    % if poskus == model.ZMAGA:
    <h1> ZMAGAL SI! </h1>
    % elif poskus == 'X':
    <h1> IZGUBIL SI </h1>
    % else:

    <form action="/igra/" method="post">
        Črka: <input type='text' name ='polje'>
        <button type="submit">Izberi polje</button>
    </form>

      <body>
  <div class="text-center"id="box">
    <header>
      <h1>Play Tic Tac Toe</h1>
    </header>
  <div id="message"></div>
    <ul id="gameBoard">
      <li class="tic"id="0">#</li>
      <li class="tic"id="1">#</li>
      <li class="tic"id="2">#</li>
      <li class="tic"id="3">#</li>
      <li class="tic"id="4">#</li>
      <li class="tic"id="5">#</li>
      <li class="tic"id="6">#</li>
      <li class="tic"id="7">#</li>
      <li class="tic"id="8">#</li>
    </ul>
    <div class="clearfix"></div>
  </div>
  </body>
    % end

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>