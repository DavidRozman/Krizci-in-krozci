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

    % end

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>