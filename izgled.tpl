
%sirina_polja = 3
%visina_polja = 3
%poskus = 'abcd'

% import model

    <h1> Križci in Krožci </h1>


    % if poskus == model.ZMAGA:
    <h1> ZMAGAL SI! </h1>
    % elif poskus == 'X':
    <h1> IZGUBIL SI </h1>
    % else:
      <table>
      %polje = 1
      % for st in range(visina_polja):
       <tr>
        % for st1 in range(sirina_polja):
            <td>
              <form action="/igra/"> 
                <button type = "submit" input type="hidden" name=polje>{{polje}}</button>
              </form>
            </td>
            %polje += 1
        % end
        </tr>
      % end
      </table>



    % end

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>