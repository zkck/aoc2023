-module(tut1).
-export([main/0]).

parse_line(Line) ->
  lists:map(fun(I) -> erlang:list_to_integer(I) end, string:split(Line, " ", all)).

parse_stdin() ->
  case io:get_line("") of
    eof -> [];
    Line -> [parse_line(string:trim(Line)) | parse_stdin()]
  end.

expand(TestCase) ->
  [H | _] = TestCase,
  AllZeros = lists:all(fun(I) -> I == 0 end, H),
  if AllZeros ->
       TestCase;
    true ->
       [_ | Tail] = H,
       expand([lists:map(fun({I1, I2}) -> I2 - I1 end, lists:zip(H, Tail, trim)) | TestCase])
  end.

solve_testcase(TestCase) ->
  ListOfLists = expand([TestCase]),
  lists:foldr(fun(L, Accu) -> Accu + lists:last(L) end, 0, ListOfLists).


main() ->
  SolvedTestCases = lists:map(fun(T) -> solve_testcase(T) end, parse_stdin()),
  erlang:display(lists:sum(SolvedTestCases)).
