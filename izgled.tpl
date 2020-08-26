
%sirina_polja = 3
%visina_polja = 2
%poskus = 'abcd'

% import model

    <h1> Križci in Krožci </h1>


    % if poskus == model.ZMAGA:
    <h1> ZMAGAL SI! </h1>
    % elif poskus == 'X':
    <h1> IZGUBIL SI </h1>
    % else:

      <form action="/igra/" method="post">
          Črka: <input type='text' name ='polje'>
          <button type="submit">Izberi polje</button>
      </form>

      <table>
      % for st in range(visina_polja):
       <tr>
        % for st1 in range(sirina_polja):
            <td>
              {{(st, st1)}}
            </td>
        % end
        </tr>
      % end
      </table>



    % end

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>