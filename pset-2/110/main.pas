program sort(input,output);
var
a,b,c,d,e,f : integer;
begin
    readln(a,b,c,d,e,f);
    if a < b then
        if b < c then
            if c < d then
                if d < e then
                    if e < f then
                        writeln(a,b,c,d,e,f)
                    else
                    if d < f then
                        writeln(a,b,c,d,f,e)
                    else
                    if c < f then
                        writeln(a,b,c,f,d,e)
                    else
                    if b < f then
                        writeln(a,b,f,c,d,e)
                    else
                    if a < f then
                        writeln(a,f,b,c,d,e)
                    else
                        writeln(f,a,b,c,d,e)
                else
                if c < e then
                    if d < f then
                        writeln(a,b,c,e,d,f)
                    else
                    if e < f then
                        writeln(a,b,c,e,f,d)
                    else
                    if c < f then
                        writeln(a,b,c,f,e,d)
                    else
                    if b < f then
                        writeln(a,b,f,c,e,d)
                    else
                    if a < f then
                        writeln(a,f,b,c,e,d)
                    else
                        writeln(f,a,b,c,e,d)
                else
                if b < e then
                    if d < f then
                        writeln(a,b,e,c,d,f)
                    else
                    if c < f then
                        writeln(a,b,e,c,f,d)
                    else
                    if e < f then
                        writeln(a,b,e,f,c,d)
                    else
                    if b < f then
                        writeln(a,b,f,e,c,d)
                    else
                    if a < f then
                        writeln(a,f,b,e,c,d)
                    else
                        writeln(f,a,b,e,c,d)
                else
                if a < e then
                    if d < f then
                        writeln(a,e,b,c,d,f)
                    else
                    if c < f then
                        writeln(a,e,b,c,f,d)
                    else
                    if b < f then
                        writeln(a,e,b,f,c,d)
                    else
                    if e < f then
                        writeln(a,e,f,b,c,d)
                    else
                    if a < f then
                        writeln(a,f,e,b,c,d)
                    else
                        writeln(f,a,e,b,c,d)
                else
                    if d < f then
                        writeln(e,a,b,c,d,f)
                    else
                    if c < f then
                        writeln(e,a,b,c,f,d)
                    else
                    if b < f then
                        writeln(e,a,b,f,c,d)
                    else
                    if a < f then
                        writeln(e,a,f,b,c,d)
                    else
                    if e < f then
                        writeln(e,f,a,b,c,d)
                    else
                        writeln(f,e,a,b,c,d)
            else
            if b < d then
                if c < f then
                    if f < e then
                        writeln(a,b,d,c,f,e)
                    else
                    if c < e then
                        writeln(a,b,d,c,e,f)
                    else
                    if d < e then
                        writeln(a,b,d,e,c,f)
                    else
                    if b < e then
                        writeln(a,b,e,d,c,f)
                    else
                    if a < e then
                        writeln(a,e,b,d,c,f)
                    else
                        writeln(e,a,b,d,c,f)
                else
                if d < f then
                    if c < e then
                        writeln(a,b,d,f,c,e)
                    else
                    if f < e then
                        writeln(a,b,d,f,e,c)
                    else
                    if d < e then
                        writeln(a,b,d,e,f,c)
                    else
                    if b < e then
                        writeln(a,b,e,d,f,c)
                    else
                    if a < e then
                        writeln(a,e,b,d,f,c)
                    else
                        writeln(e,a,b,d,f,c)
                else
                if b < f then
                    if c < e then
                        writeln(a,b,f,d,c,e)
                    else
                    if d < e then
                        writeln(a,b,f,d,e,c)
                    else
                    if f < e then
                        writeln(a,b,f,e,d,c)
                    else
                    if b < e then
                        writeln(a,b,e,f,d,c)
                    else
                    if a < e then
                        writeln(a,e,b,f,d,c)
                    else
                        writeln(e,a,b,f,d,c)
                else
                if a < f then
                    if c < e then
                        writeln(a,f,b,d,c,e)
                    else
                    if d < e then
                        writeln(a,f,b,d,e,c)
                    else
                    if b < e then
                        writeln(a,f,b,e,d,c)
                    else
                    if f < e then
                        writeln(a,f,e,b,d,c)
                    else
                    if a < e then
                        writeln(a,e,f,b,d,c)
                    else
                        writeln(e,a,f,b,d,c)
                else
                    if c < e then
                        writeln(f,a,b,d,c,e)
                    else
                    if d < e then
                        writeln(f,a,b,d,e,c)
                    else
                    if b < e then
                        writeln(f,a,b,e,d,c)
                    else
                    if a < e then
                        writeln(f,a,e,b,d,c)
                    else
                    if f < e then
                        writeln(f,e,a,b,d,c)
                    else
                        writeln(e,f,a,b,d,c)
            else
            if a < d then
                if c < e then
                    if e < f then
                        writeln(a,d,b,c,e,f)
                    else
                    if c < f then
                        writeln(a,d,b,c,f,e)
                    else
                    if b < f then
                        writeln(a,d,b,f,c,e)
                    else
                    if d < f then
                        writeln(a,d,f,b,c,e)
                    else
                    if a < f then
                        writeln(a,f,d,b,c,e)
                    else
                        writeln(f,a,d,b,c,e)
                else
                if b < e then
                    if c < f then
                        writeln(a,d,b,e,c,f)
                    else
                    if e < f then
                        writeln(a,d,b,e,f,c)
                    else
                    if b < f then
                        writeln(a,d,b,f,e,c)
                    else
                    if d < f then
                        writeln(a,d,f,b,e,c)
                    else
                    if a < f then
                        writeln(a,f,d,b,e,c)
                    else
                        writeln(f,a,d,b,e,c)
                else
                if d < e then
                    if c < f then
                        writeln(a,d,e,b,c,f)
                    else
                    if b < f then
                        writeln(a,d,e,b,f,c)
                    else
                    if e < f then
                        writeln(a,d,e,f,b,c)
                    else
                    if d < f then
                        writeln(a,d,f,e,b,c)
                    else
                    if a < f then
                        writeln(a,f,d,e,b,c)
                    else
                        writeln(f,a,d,e,b,c)
                else
                if a < e then
                    if c < f then
                        writeln(a,e,d,b,c,f)
                    else
                    if b < f then
                        writeln(a,e,d,b,f,c)
                    else
                    if d < f then
                        writeln(a,e,d,f,b,c)
                    else
                    if e < f then
                        writeln(a,e,f,d,b,c)
                    else
                    if a < f then
                        writeln(a,f,e,d,b,c)
                    else
                        writeln(f,a,e,d,b,c)
                else
                    if c < f then
                        writeln(e,a,d,b,c,f)
                    else
                    if b < f then
                        writeln(e,a,d,b,f,c)
                    else
                    if d < f then
                        writeln(e,a,d,f,b,c)
                    else
                    if a < f then
                        writeln(e,a,f,d,b,c)
                    else
                    if e < f then
                        writeln(e,f,a,d,b,c)
                    else
                        writeln(f,e,a,d,b,c)
            else
                if c < f then
                    if f < e then
                        writeln(d,a,b,c,f,e)
                    else
                    if c < e then
                        writeln(d,a,b,c,e,f)
                    else
                    if b < e then
                        writeln(d,a,b,e,c,f)
                    else
                    if a < e then
                        writeln(d,a,e,b,c,f)
                    else
                    if d < e then
                        writeln(d,e,a,b,c,f)
                    else
                        writeln(e,d,a,b,c,f)
                else
                if b < f then
                    if c < e then
                        writeln(d,a,b,f,c,e)
                    else
                    if f < e then
                        writeln(d,a,b,f,e,c)
                    else
                    if b < e then
                        writeln(d,a,b,e,f,c)
                    else
                    if a < e then
                        writeln(d,a,e,b,f,c)
                    else
                    if d < e then
                        writeln(d,e,a,b,f,c)
                    else
                        writeln(e,d,a,b,f,c)
                else
                if a < f then
                    if c < e then
                        writeln(d,a,f,b,c,e)
                    else
                    if b < e then
                        writeln(d,a,f,b,e,c)
                    else
                    if f < e then
                        writeln(d,a,f,e,b,c)
                    else
                    if a < e then
                        writeln(d,a,e,f,b,c)
                    else
                    if d < e then
                        writeln(d,e,a,f,b,c)
                    else
                        writeln(e,d,a,f,b,c)
                else
                if d < f then
                    if c < e then
                        writeln(d,f,a,b,c,e)
                    else
                    if b < e then
                        writeln(d,f,a,b,e,c)
                    else
                    if a < e then
                        writeln(d,f,a,e,b,c)
                    else
                    if f < e then
                        writeln(d,f,e,a,b,c)
                    else
                    if d < e then
                        writeln(d,e,f,a,b,c)
                    else
                        writeln(e,d,f,a,b,c)
                else
                    if c < e then
                        writeln(f,d,a,b,c,e)
                    else
                    if b < e then
                        writeln(f,d,a,b,e,c)
                    else
                    if a < e then
                        writeln(f,d,a,e,b,c)
                    else
                    if d < e then
                        writeln(f,d,e,a,b,c)
                    else
                    if f < e then
                        writeln(f,e,d,a,b,c)
                    else
                        writeln(e,f,d,a,b,c)
        else
        if a < c then
            if b < e then
                if e < f then
                    if f < d then
                        writeln(a,c,b,e,f,d)
                    else
                    if e < d then
                        writeln(a,c,b,e,d,f)
                    else
                    if b < d then
                        writeln(a,c,b,d,e,f)
                    else
                    if c < d then
                        writeln(a,c,d,b,e,f)
                    else
                    if a < d then
                        writeln(a,d,c,b,e,f)
                    else
                        writeln(d,a,c,b,e,f)
                else
                if b < f then
                    if e < d then
                        writeln(a,c,b,f,e,d)
                    else
                    if f < d then
                        writeln(a,c,b,f,d,e)
                    else
                    if b < d then
                        writeln(a,c,b,d,f,e)
                    else
                    if c < d then
                        writeln(a,c,d,b,f,e)
                    else
                    if a < d then
                        writeln(a,d,c,b,f,e)
                    else
                        writeln(d,a,c,b,f,e)
                else
                if c < f then
                    if e < d then
                        writeln(a,c,f,b,e,d)
                    else
                    if b < d then
                        writeln(a,c,f,b,d,e)
                    else
                    if f < d then
                        writeln(a,c,f,d,b,e)
                    else
                    if c < d then
                        writeln(a,c,d,f,b,e)
                    else
                    if a < d then
                        writeln(a,d,c,f,b,e)
                    else
                        writeln(d,a,c,f,b,e)
                else
                if a < f then
                    if e < d then
                        writeln(a,f,c,b,e,d)
                    else
                    if b < d then
                        writeln(a,f,c,b,d,e)
                    else
                    if c < d then
                        writeln(a,f,c,d,b,e)
                    else
                    if f < d then
                        writeln(a,f,d,c,b,e)
                    else
                    if a < d then
                        writeln(a,d,f,c,b,e)
                    else
                        writeln(d,a,f,c,b,e)
                else
                    if e < d then
                        writeln(f,a,c,b,e,d)
                    else
                    if b < d then
                        writeln(f,a,c,b,d,e)
                    else
                    if c < d then
                        writeln(f,a,c,d,b,e)
                    else
                    if a < d then
                        writeln(f,a,d,c,b,e)
                    else
                    if f < d then
                        writeln(f,d,a,c,b,e)
                    else
                        writeln(d,f,a,c,b,e)
            else
            if c < e then
                if b < d then
                    if d < f then
                        writeln(a,c,e,b,d,f)
                    else
                    if b < f then
                        writeln(a,c,e,b,f,d)
                    else
                    if e < f then
                        writeln(a,c,e,f,b,d)
                    else
                    if c < f then
                        writeln(a,c,f,e,b,d)
                    else
                    if a < f then
                        writeln(a,f,c,e,b,d)
                    else
                        writeln(f,a,c,e,b,d)
                else
                if e < d then
                    if b < f then
                        writeln(a,c,e,d,b,f)
                    else
                    if d < f then
                        writeln(a,c,e,d,f,b)
                    else
                    if e < f then
                        writeln(a,c,e,f,d,b)
                    else
                    if c < f then
                        writeln(a,c,f,e,d,b)
                    else
                    if a < f then
                        writeln(a,f,c,e,d,b)
                    else
                        writeln(f,a,c,e,d,b)
                else
                if c < d then
                    if b < f then
                        writeln(a,c,d,e,b,f)
                    else
                    if e < f then
                        writeln(a,c,d,e,f,b)
                    else
                    if d < f then
                        writeln(a,c,d,f,e,b)
                    else
                    if c < f then
                        writeln(a,c,f,d,e,b)
                    else
                    if a < f then
                        writeln(a,f,c,d,e,b)
                    else
                        writeln(f,a,c,d,e,b)
                else
                if a < d then
                    if b < f then
                        writeln(a,d,c,e,b,f)
                    else
                    if e < f then
                        writeln(a,d,c,e,f,b)
                    else
                    if c < f then
                        writeln(a,d,c,f,e,b)
                    else
                    if d < f then
                        writeln(a,d,f,c,e,b)
                    else
                    if a < f then
                        writeln(a,f,d,c,e,b)
                    else
                        writeln(f,a,d,c,e,b)
                else
                    if b < f then
                        writeln(d,a,c,e,b,f)
                    else
                    if e < f then
                        writeln(d,a,c,e,f,b)
                    else
                    if c < f then
                        writeln(d,a,c,f,e,b)
                    else
                    if a < f then
                        writeln(d,a,f,c,e,b)
                    else
                    if d < f then
                        writeln(d,f,a,c,e,b)
                    else
                        writeln(f,d,a,c,e,b)
            else
            if a < e then
                if b < f then
                    if f < d then
                        writeln(a,e,c,b,f,d)
                    else
                    if b < d then
                        writeln(a,e,c,b,d,f)
                    else
                    if c < d then
                        writeln(a,e,c,d,b,f)
                    else
                    if e < d then
                        writeln(a,e,d,c,b,f)
                    else
                    if a < d then
                        writeln(a,d,e,c,b,f)
                    else
                        writeln(d,a,e,c,b,f)
                else
                if c < f then
                    if b < d then
                        writeln(a,e,c,f,b,d)
                    else
                    if f < d then
                        writeln(a,e,c,f,d,b)
                    else
                    if c < d then
                        writeln(a,e,c,d,f,b)
                    else
                    if e < d then
                        writeln(a,e,d,c,f,b)
                    else
                    if a < d then
                        writeln(a,d,e,c,f,b)
                    else
                        writeln(d,a,e,c,f,b)
                else
                if e < f then
                    if b < d then
                        writeln(a,e,f,c,b,d)
                    else
                    if c < d then
                        writeln(a,e,f,c,d,b)
                    else
                    if f < d then
                        writeln(a,e,f,d,c,b)
                    else
                    if e < d then
                        writeln(a,e,d,f,c,b)
                    else
                    if a < d then
                        writeln(a,d,e,f,c,b)
                    else
                        writeln(d,a,e,f,c,b)
                else
                if a < f then
                    if b < d then
                        writeln(a,f,e,c,b,d)
                    else
                    if c < d then
                        writeln(a,f,e,c,d,b)
                    else
                    if e < d then
                        writeln(a,f,e,d,c,b)
                    else
                    if f < d then
                        writeln(a,f,d,e,c,b)
                    else
                    if a < d then
                        writeln(a,d,f,e,c,b)
                    else
                        writeln(d,a,f,e,c,b)
                else
                    if b < d then
                        writeln(f,a,e,c,b,d)
                    else
                    if c < d then
                        writeln(f,a,e,c,d,b)
                    else
                    if e < d then
                        writeln(f,a,e,d,c,b)
                    else
                    if a < d then
                        writeln(f,a,d,e,c,b)
                    else
                    if f < d then
                        writeln(f,d,a,e,c,b)
                    else
                        writeln(d,f,a,e,c,b)
            else
                if b < d then
                    if d < f then
                        writeln(e,a,c,b,d,f)
                    else
                    if b < f then
                        writeln(e,a,c,b,f,d)
                    else
                    if c < f then
                        writeln(e,a,c,f,b,d)
                    else
                    if a < f then
                        writeln(e,a,f,c,b,d)
                    else
                    if e < f then
                        writeln(e,f,a,c,b,d)
                    else
                        writeln(f,e,a,c,b,d)
                else
                if c < d then
                    if b < f then
                        writeln(e,a,c,d,b,f)
                    else
                    if d < f then
                        writeln(e,a,c,d,f,b)
                    else
                    if c < f then
                        writeln(e,a,c,f,d,b)
                    else
                    if a < f then
                        writeln(e,a,f,c,d,b)
                    else
                    if e < f then
                        writeln(e,f,a,c,d,b)
                    else
                        writeln(f,e,a,c,d,b)
                else
                if a < d then
                    if b < f then
                        writeln(e,a,d,c,b,f)
                    else
                    if c < f then
                        writeln(e,a,d,c,f,b)
                    else
                    if d < f then
                        writeln(e,a,d,f,c,b)
                    else
                    if a < f then
                        writeln(e,a,f,d,c,b)
                    else
                    if e < f then
                        writeln(e,f,a,d,c,b)
                    else
                        writeln(f,e,a,d,c,b)
                else
                if e < d then
                    if b < f then
                        writeln(e,d,a,c,b,f)
                    else
                    if c < f then
                        writeln(e,d,a,c,f,b)
                    else
                    if a < f then
                        writeln(e,d,a,f,c,b)
                    else
                    if d < f then
                        writeln(e,d,f,a,c,b)
                    else
                    if e < f then
                        writeln(e,f,d,a,c,b)
                    else
                        writeln(f,e,d,a,c,b)
                else
                    if b < f then
                        writeln(d,e,a,c,b,f)
                    else
                    if c < f then
                        writeln(d,e,a,c,f,b)
                    else
                    if a < f then
                        writeln(d,e,a,f,c,b)
                    else
                    if e < f then
                        writeln(d,e,f,a,c,b)
                    else
                    if d < f then
                        writeln(d,f,e,a,c,b)
                    else
                        writeln(f,d,e,a,c,b)
        else
            if b < f then
                if f < d then
                    if d < e then
                        writeln(c,a,b,f,d,e)
                    else
                    if f < e then
                        writeln(c,a,b,f,e,d)
                    else
                    if b < e then
                        writeln(c,a,b,e,f,d)
                    else
                    if a < e then
                        writeln(c,a,e,b,f,d)
                    else
                    if c < e then
                        writeln(c,e,a,b,f,d)
                    else
                        writeln(e,c,a,b,f,d)
                else
                if b < d then
                    if f < e then
                        writeln(c,a,b,d,f,e)
                    else
                    if d < e then
                        writeln(c,a,b,d,e,f)
                    else
                    if b < e then
                        writeln(c,a,b,e,d,f)
                    else
                    if a < e then
                        writeln(c,a,e,b,d,f)
                    else
                    if c < e then
                        writeln(c,e,a,b,d,f)
                    else
                        writeln(e,c,a,b,d,f)
                else
                if a < d then
                    if f < e then
                        writeln(c,a,d,b,f,e)
                    else
                    if b < e then
                        writeln(c,a,d,b,e,f)
                    else
                    if d < e then
                        writeln(c,a,d,e,b,f)
                    else
                    if a < e then
                        writeln(c,a,e,d,b,f)
                    else
                    if c < e then
                        writeln(c,e,a,d,b,f)
                    else
                        writeln(e,c,a,d,b,f)
                else
                if c < d then
                    if f < e then
                        writeln(c,d,a,b,f,e)
                    else
                    if b < e then
                        writeln(c,d,a,b,e,f)
                    else
                    if a < e then
                        writeln(c,d,a,e,b,f)
                    else
                    if d < e then
                        writeln(c,d,e,a,b,f)
                    else
                    if c < e then
                        writeln(c,e,d,a,b,f)
                    else
                        writeln(e,c,d,a,b,f)
                else
                    if f < e then
                        writeln(d,c,a,b,f,e)
                    else
                    if b < e then
                        writeln(d,c,a,b,e,f)
                    else
                    if a < e then
                        writeln(d,c,a,e,b,f)
                    else
                    if c < e then
                        writeln(d,c,e,a,b,f)
                    else
                    if d < e then
                        writeln(d,e,c,a,b,f)
                    else
                        writeln(e,d,c,a,b,f)
            else
            if a < f then
                if b < e then
                    if e < d then
                        writeln(c,a,f,b,e,d)
                    else
                    if b < d then
                        writeln(c,a,f,b,d,e)
                    else
                    if f < d then
                        writeln(c,a,f,d,b,e)
                    else
                    if a < d then
                        writeln(c,a,d,f,b,e)
                    else
                    if c < d then
                        writeln(c,d,a,f,b,e)
                    else
                        writeln(d,c,a,f,b,e)
                else
                if f < e then
                    if b < d then
                        writeln(c,a,f,e,b,d)
                    else
                    if e < d then
                        writeln(c,a,f,e,d,b)
                    else
                    if f < d then
                        writeln(c,a,f,d,e,b)
                    else
                    if a < d then
                        writeln(c,a,d,f,e,b)
                    else
                    if c < d then
                        writeln(c,d,a,f,e,b)
                    else
                        writeln(d,c,a,f,e,b)
                else
                if a < e then
                    if b < d then
                        writeln(c,a,e,f,b,d)
                    else
                    if f < d then
                        writeln(c,a,e,f,d,b)
                    else
                    if e < d then
                        writeln(c,a,e,d,f,b)
                    else
                    if a < d then
                        writeln(c,a,d,e,f,b)
                    else
                    if c < d then
                        writeln(c,d,a,e,f,b)
                    else
                        writeln(d,c,a,e,f,b)
                else
                if c < e then
                    if b < d then
                        writeln(c,e,a,f,b,d)
                    else
                    if f < d then
                        writeln(c,e,a,f,d,b)
                    else
                    if a < d then
                        writeln(c,e,a,d,f,b)
                    else
                    if e < d then
                        writeln(c,e,d,a,f,b)
                    else
                    if c < d then
                        writeln(c,d,e,a,f,b)
                    else
                        writeln(d,c,e,a,f,b)
                else
                    if b < d then
                        writeln(e,c,a,f,b,d)
                    else
                    if f < d then
                        writeln(e,c,a,f,d,b)
                    else
                    if a < d then
                        writeln(e,c,a,d,f,b)
                    else
                    if c < d then
                        writeln(e,c,d,a,f,b)
                    else
                    if e < d then
                        writeln(e,d,c,a,f,b)
                    else
                        writeln(d,e,c,a,f,b)
            else
            if c < f then
                if b < d then
                    if d < e then
                        writeln(c,f,a,b,d,e)
                    else
                    if b < e then
                        writeln(c,f,a,b,e,d)
                    else
                    if a < e then
                        writeln(c,f,a,e,b,d)
                    else
                    if f < e then
                        writeln(c,f,e,a,b,d)
                    else
                    if c < e then
                        writeln(c,e,f,a,b,d)
                    else
                        writeln(e,c,f,a,b,d)
                else
                if a < d then
                    if b < e then
                        writeln(c,f,a,d,b,e)
                    else
                    if d < e then
                        writeln(c,f,a,d,e,b)
                    else
                    if a < e then
                        writeln(c,f,a,e,d,b)
                    else
                    if f < e then
                        writeln(c,f,e,a,d,b)
                    else
                    if c < e then
                        writeln(c,e,f,a,d,b)
                    else
                        writeln(e,c,f,a,d,b)
                else
                if f < d then
                    if b < e then
                        writeln(c,f,d,a,b,e)
                    else
                    if a < e then
                        writeln(c,f,d,a,e,b)
                    else
                    if d < e then
                        writeln(c,f,d,e,a,b)
                    else
                    if f < e then
                        writeln(c,f,e,d,a,b)
                    else
                    if c < e then
                        writeln(c,e,f,d,a,b)
                    else
                        writeln(e,c,f,d,a,b)
                else
                if c < d then
                    if b < e then
                        writeln(c,d,f,a,b,e)
                    else
                    if a < e then
                        writeln(c,d,f,a,e,b)
                    else
                    if f < e then
                        writeln(c,d,f,e,a,b)
                    else
                    if d < e then
                        writeln(c,d,e,f,a,b)
                    else
                    if c < e then
                        writeln(c,e,d,f,a,b)
                    else
                        writeln(e,c,d,f,a,b)
                else
                    if b < e then
                        writeln(d,c,f,a,b,e)
                    else
                    if a < e then
                        writeln(d,c,f,a,e,b)
                    else
                    if f < e then
                        writeln(d,c,f,e,a,b)
                    else
                    if c < e then
                        writeln(d,c,e,f,a,b)
                    else
                    if d < e then
                        writeln(d,e,c,f,a,b)
                    else
                        writeln(e,d,c,f,a,b)
            else
                if b < e then
                    if e < d then
                        writeln(f,c,a,b,e,d)
                    else
                    if b < d then
                        writeln(f,c,a,b,d,e)
                    else
                    if a < d then
                        writeln(f,c,a,d,b,e)
                    else
                    if c < d then
                        writeln(f,c,d,a,b,e)
                    else
                    if f < d then
                        writeln(f,d,c,a,b,e)
                    else
                        writeln(d,f,c,a,b,e)
                else
                if a < e then
                    if b < d then
                        writeln(f,c,a,e,b,d)
                    else
                    if e < d then
                        writeln(f,c,a,e,d,b)
                    else
                    if a < d then
                        writeln(f,c,a,d,e,b)
                    else
                    if c < d then
                        writeln(f,c,d,a,e,b)
                    else
                    if f < d then
                        writeln(f,d,c,a,e,b)
                    else
                        writeln(d,f,c,a,e,b)
                else
                if c < e then
                    if b < d then
                        writeln(f,c,e,a,b,d)
                    else
                    if a < d then
                        writeln(f,c,e,a,d,b)
                    else
                    if e < d then
                        writeln(f,c,e,d,a,b)
                    else
                    if c < d then
                        writeln(f,c,d,e,a,b)
                    else
                    if f < d then
                        writeln(f,d,c,e,a,b)
                    else
                        writeln(d,f,c,e,a,b)
                else
                if f < e then
                    if b < d then
                        writeln(f,e,c,a,b,d)
                    else
                    if a < d then
                        writeln(f,e,c,a,d,b)
                    else
                    if c < d then
                        writeln(f,e,c,d,a,b)
                    else
                    if e < d then
                        writeln(f,e,d,c,a,b)
                    else
                    if f < d then
                        writeln(f,d,e,c,a,b)
                    else
                        writeln(d,f,e,c,a,b)
                else
                    if b < d then
                        writeln(e,f,c,a,b,d)
                    else
                    if a < d then
                        writeln(e,f,c,a,d,b)
                    else
                    if c < d then
                        writeln(e,f,c,d,a,b)
                    else
                    if f < d then
                        writeln(e,f,d,c,a,b)
                    else
                    if e < d then
                        writeln(e,d,f,c,a,b)
                    else
                        writeln(d,e,f,c,a,b)
    else
        if a < d then
            if d < e then
                if e < f then
                    if f < c then
                        writeln(b,a,d,e,f,c)
                    else
                    if e < c then
                        writeln(b,a,d,e,c,f)
                    else
                    if d < c then
                        writeln(b,a,d,c,e,f)
                    else
                    if a < c then
                        writeln(b,a,c,d,e,f)
                    else
                    if b < c then
                        writeln(b,c,a,d,e,f)
                    else
                        writeln(c,b,a,d,e,f)
                else
                if d < f then
                    if e < c then
                        writeln(b,a,d,f,e,c)
                    else
                    if f < c then
                        writeln(b,a,d,f,c,e)
                    else
                    if d < c then
                        writeln(b,a,d,c,f,e)
                    else
                    if a < c then
                        writeln(b,a,c,d,f,e)
                    else
                    if b < c then
                        writeln(b,c,a,d,f,e)
                    else
                        writeln(c,b,a,d,f,e)
                else
                if a < f then
                    if e < c then
                        writeln(b,a,f,d,e,c)
                    else
                    if d < c then
                        writeln(b,a,f,d,c,e)
                    else
                    if f < c then
                        writeln(b,a,f,c,d,e)
                    else
                    if a < c then
                        writeln(b,a,c,f,d,e)
                    else
                    if b < c then
                        writeln(b,c,a,f,d,e)
                    else
                        writeln(c,b,a,f,d,e)
                else
                if b < f then
                    if e < c then
                        writeln(b,f,a,d,e,c)
                    else
                    if d < c then
                        writeln(b,f,a,d,c,e)
                    else
                    if a < c then
                        writeln(b,f,a,c,d,e)
                    else
                    if f < c then
                        writeln(b,f,c,a,d,e)
                    else
                    if b < c then
                        writeln(b,c,f,a,d,e)
                    else
                        writeln(c,b,f,a,d,e)
                else
                    if e < c then
                        writeln(f,b,a,d,e,c)
                    else
                    if d < c then
                        writeln(f,b,a,d,c,e)
                    else
                    if a < c then
                        writeln(f,b,a,c,d,e)
                    else
                    if b < c then
                        writeln(f,b,c,a,d,e)
                    else
                    if f < c then
                        writeln(f,c,b,a,d,e)
                    else
                        writeln(c,f,b,a,d,e)
            else
            if a < e then
                if d < c then
                    if c < f then
                        writeln(b,a,e,d,c,f)
                    else
                    if d < f then
                        writeln(b,a,e,d,f,c)
                    else
                    if e < f then
                        writeln(b,a,e,f,d,c)
                    else
                    if a < f then
                        writeln(b,a,f,e,d,c)
                    else
                    if b < f then
                        writeln(b,f,a,e,d,c)
                    else
                        writeln(f,b,a,e,d,c)
                else
                if e < c then
                    if d < f then
                        writeln(b,a,e,c,d,f)
                    else
                    if c < f then
                        writeln(b,a,e,c,f,d)
                    else
                    if e < f then
                        writeln(b,a,e,f,c,d)
                    else
                    if a < f then
                        writeln(b,a,f,e,c,d)
                    else
                    if b < f then
                        writeln(b,f,a,e,c,d)
                    else
                        writeln(f,b,a,e,c,d)
                else
                if a < c then
                    if d < f then
                        writeln(b,a,c,e,d,f)
                    else
                    if e < f then
                        writeln(b,a,c,e,f,d)
                    else
                    if c < f then
                        writeln(b,a,c,f,e,d)
                    else
                    if a < f then
                        writeln(b,a,f,c,e,d)
                    else
                    if b < f then
                        writeln(b,f,a,c,e,d)
                    else
                        writeln(f,b,a,c,e,d)
                else
                if b < c then
                    if d < f then
                        writeln(b,c,a,e,d,f)
                    else
                    if e < f then
                        writeln(b,c,a,e,f,d)
                    else
                    if a < f then
                        writeln(b,c,a,f,e,d)
                    else
                    if c < f then
                        writeln(b,c,f,a,e,d)
                    else
                    if b < f then
                        writeln(b,f,c,a,e,d)
                    else
                        writeln(f,b,c,a,e,d)
                else
                    if d < f then
                        writeln(c,b,a,e,d,f)
                    else
                    if e < f then
                        writeln(c,b,a,e,f,d)
                    else
                    if a < f then
                        writeln(c,b,a,f,e,d)
                    else
                    if b < f then
                        writeln(c,b,f,a,e,d)
                    else
                    if c < f then
                        writeln(c,f,b,a,e,d)
                    else
                        writeln(f,c,b,a,e,d)
            else
            if b < e then
                if d < f then
                    if f < c then
                        writeln(b,e,a,d,f,c)
                    else
                    if d < c then
                        writeln(b,e,a,d,c,f)
                    else
                    if a < c then
                        writeln(b,e,a,c,d,f)
                    else
                    if e < c then
                        writeln(b,e,c,a,d,f)
                    else
                    if b < c then
                        writeln(b,c,e,a,d,f)
                    else
                        writeln(c,b,e,a,d,f)
                else
                if a < f then
                    if d < c then
                        writeln(b,e,a,f,d,c)
                    else
                    if f < c then
                        writeln(b,e,a,f,c,d)
                    else
                    if a < c then
                        writeln(b,e,a,c,f,d)
                    else
                    if e < c then
                        writeln(b,e,c,a,f,d)
                    else
                    if b < c then
                        writeln(b,c,e,a,f,d)
                    else
                        writeln(c,b,e,a,f,d)
                else
                if e < f then
                    if d < c then
                        writeln(b,e,f,a,d,c)
                    else
                    if a < c then
                        writeln(b,e,f,a,c,d)
                    else
                    if f < c then
                        writeln(b,e,f,c,a,d)
                    else
                    if e < c then
                        writeln(b,e,c,f,a,d)
                    else
                    if b < c then
                        writeln(b,c,e,f,a,d)
                    else
                        writeln(c,b,e,f,a,d)
                else
                if b < f then
                    if d < c then
                        writeln(b,f,e,a,d,c)
                    else
                    if a < c then
                        writeln(b,f,e,a,c,d)
                    else
                    if e < c then
                        writeln(b,f,e,c,a,d)
                    else
                    if f < c then
                        writeln(b,f,c,e,a,d)
                    else
                    if b < c then
                        writeln(b,c,f,e,a,d)
                    else
                        writeln(c,b,f,e,a,d)
                else
                    if d < c then
                        writeln(f,b,e,a,d,c)
                    else
                    if a < c then
                        writeln(f,b,e,a,c,d)
                    else
                    if e < c then
                        writeln(f,b,e,c,a,d)
                    else
                    if b < c then
                        writeln(f,b,c,e,a,d)
                    else
                    if f < c then
                        writeln(f,c,b,e,a,d)
                    else
                        writeln(c,f,b,e,a,d)
            else
                if d < c then
                    if c < f then
                        writeln(e,b,a,d,c,f)
                    else
                    if d < f then
                        writeln(e,b,a,d,f,c)
                    else
                    if a < f then
                        writeln(e,b,a,f,d,c)
                    else
                    if b < f then
                        writeln(e,b,f,a,d,c)
                    else
                    if e < f then
                        writeln(e,f,b,a,d,c)
                    else
                        writeln(f,e,b,a,d,c)
                else
                if a < c then
                    if d < f then
                        writeln(e,b,a,c,d,f)
                    else
                    if c < f then
                        writeln(e,b,a,c,f,d)
                    else
                    if a < f then
                        writeln(e,b,a,f,c,d)
                    else
                    if b < f then
                        writeln(e,b,f,a,c,d)
                    else
                    if e < f then
                        writeln(e,f,b,a,c,d)
                    else
                        writeln(f,e,b,a,c,d)
                else
                if b < c then
                    if d < f then
                        writeln(e,b,c,a,d,f)
                    else
                    if a < f then
                        writeln(e,b,c,a,f,d)
                    else
                    if c < f then
                        writeln(e,b,c,f,a,d)
                    else
                    if b < f then
                        writeln(e,b,f,c,a,d)
                    else
                    if e < f then
                        writeln(e,f,b,c,a,d)
                    else
                        writeln(f,e,b,c,a,d)
                else
                if e < c then
                    if d < f then
                        writeln(e,c,b,a,d,f)
                    else
                    if a < f then
                        writeln(e,c,b,a,f,d)
                    else
                    if b < f then
                        writeln(e,c,b,f,a,d)
                    else
                    if c < f then
                        writeln(e,c,f,b,a,d)
                    else
                    if e < f then
                        writeln(e,f,c,b,a,d)
                    else
                        writeln(f,e,c,b,a,d)
                else
                    if d < f then
                        writeln(c,e,b,a,d,f)
                    else
                    if a < f then
                        writeln(c,e,b,a,f,d)
                    else
                    if b < f then
                        writeln(c,e,b,f,a,d)
                    else
                    if e < f then
                        writeln(c,e,f,b,a,d)
                    else
                    if c < f then
                        writeln(c,f,e,b,a,d)
                    else
                        writeln(f,c,e,b,a,d)
        else
        if b < d then
            if a < f then
                if f < c then
                    if c < e then
                        writeln(b,d,a,f,c,e)
                    else
                    if f < e then
                        writeln(b,d,a,f,e,c)
                    else
                    if a < e then
                        writeln(b,d,a,e,f,c)
                    else
                    if d < e then
                        writeln(b,d,e,a,f,c)
                    else
                    if b < e then
                        writeln(b,e,d,a,f,c)
                    else
                        writeln(e,b,d,a,f,c)
                else
                if a < c then
                    if f < e then
                        writeln(b,d,a,c,f,e)
                    else
                    if c < e then
                        writeln(b,d,a,c,e,f)
                    else
                    if a < e then
                        writeln(b,d,a,e,c,f)
                    else
                    if d < e then
                        writeln(b,d,e,a,c,f)
                    else
                    if b < e then
                        writeln(b,e,d,a,c,f)
                    else
                        writeln(e,b,d,a,c,f)
                else
                if d < c then
                    if f < e then
                        writeln(b,d,c,a,f,e)
                    else
                    if a < e then
                        writeln(b,d,c,a,e,f)
                    else
                    if c < e then
                        writeln(b,d,c,e,a,f)
                    else
                    if d < e then
                        writeln(b,d,e,c,a,f)
                    else
                    if b < e then
                        writeln(b,e,d,c,a,f)
                    else
                        writeln(e,b,d,c,a,f)
                else
                if b < c then
                    if f < e then
                        writeln(b,c,d,a,f,e)
                    else
                    if a < e then
                        writeln(b,c,d,a,e,f)
                    else
                    if d < e then
                        writeln(b,c,d,e,a,f)
                    else
                    if c < e then
                        writeln(b,c,e,d,a,f)
                    else
                    if b < e then
                        writeln(b,e,c,d,a,f)
                    else
                        writeln(e,b,c,d,a,f)
                else
                    if f < e then
                        writeln(c,b,d,a,f,e)
                    else
                    if a < e then
                        writeln(c,b,d,a,e,f)
                    else
                    if d < e then
                        writeln(c,b,d,e,a,f)
                    else
                    if b < e then
                        writeln(c,b,e,d,a,f)
                    else
                    if c < e then
                        writeln(c,e,b,d,a,f)
                    else
                        writeln(e,c,b,d,a,f)
            else
            if d < f then
                if a < e then
                    if e < c then
                        writeln(b,d,f,a,e,c)
                    else
                    if a < c then
                        writeln(b,d,f,a,c,e)
                    else
                    if f < c then
                        writeln(b,d,f,c,a,e)
                    else
                    if d < c then
                        writeln(b,d,c,f,a,e)
                    else
                    if b < c then
                        writeln(b,c,d,f,a,e)
                    else
                        writeln(c,b,d,f,a,e)
                else
                if f < e then
                    if a < c then
                        writeln(b,d,f,e,a,c)
                    else
                    if e < c then
                        writeln(b,d,f,e,c,a)
                    else
                    if f < c then
                        writeln(b,d,f,c,e,a)
                    else
                    if d < c then
                        writeln(b,d,c,f,e,a)
                    else
                    if b < c then
                        writeln(b,c,d,f,e,a)
                    else
                        writeln(c,b,d,f,e,a)
                else
                if d < e then
                    if a < c then
                        writeln(b,d,e,f,a,c)
                    else
                    if f < c then
                        writeln(b,d,e,f,c,a)
                    else
                    if e < c then
                        writeln(b,d,e,c,f,a)
                    else
                    if d < c then
                        writeln(b,d,c,e,f,a)
                    else
                    if b < c then
                        writeln(b,c,d,e,f,a)
                    else
                        writeln(c,b,d,e,f,a)
                else
                if b < e then
                    if a < c then
                        writeln(b,e,d,f,a,c)
                    else
                    if f < c then
                        writeln(b,e,d,f,c,a)
                    else
                    if d < c then
                        writeln(b,e,d,c,f,a)
                    else
                    if e < c then
                        writeln(b,e,c,d,f,a)
                    else
                    if b < c then
                        writeln(b,c,e,d,f,a)
                    else
                        writeln(c,b,e,d,f,a)
                else
                    if a < c then
                        writeln(e,b,d,f,a,c)
                    else
                    if f < c then
                        writeln(e,b,d,f,c,a)
                    else
                    if d < c then
                        writeln(e,b,d,c,f,a)
                    else
                    if b < c then
                        writeln(e,b,c,d,f,a)
                    else
                    if e < c then
                        writeln(e,c,b,d,f,a)
                    else
                        writeln(c,e,b,d,f,a)
            else
            if b < f then
                if a < c then
                    if c < e then
                        writeln(b,f,d,a,c,e)
                    else
                    if a < e then
                        writeln(b,f,d,a,e,c)
                    else
                    if d < e then
                        writeln(b,f,d,e,a,c)
                    else
                    if f < e then
                        writeln(b,f,e,d,a,c)
                    else
                    if b < e then
                        writeln(b,e,f,d,a,c)
                    else
                        writeln(e,b,f,d,a,c)
                else
                if d < c then
                    if a < e then
                        writeln(b,f,d,c,a,e)
                    else
                    if c < e then
                        writeln(b,f,d,c,e,a)
                    else
                    if d < e then
                        writeln(b,f,d,e,c,a)
                    else
                    if f < e then
                        writeln(b,f,e,d,c,a)
                    else
                    if b < e then
                        writeln(b,e,f,d,c,a)
                    else
                        writeln(e,b,f,d,c,a)
                else
                if f < c then
                    if a < e then
                        writeln(b,f,c,d,a,e)
                    else
                    if d < e then
                        writeln(b,f,c,d,e,a)
                    else
                    if c < e then
                        writeln(b,f,c,e,d,a)
                    else
                    if f < e then
                        writeln(b,f,e,c,d,a)
                    else
                    if b < e then
                        writeln(b,e,f,c,d,a)
                    else
                        writeln(e,b,f,c,d,a)
                else
                if b < c then
                    if a < e then
                        writeln(b,c,f,d,a,e)
                    else
                    if d < e then
                        writeln(b,c,f,d,e,a)
                    else
                    if f < e then
                        writeln(b,c,f,e,d,a)
                    else
                    if c < e then
                        writeln(b,c,e,f,d,a)
                    else
                    if b < e then
                        writeln(b,e,c,f,d,a)
                    else
                        writeln(e,b,c,f,d,a)
                else
                    if a < e then
                        writeln(c,b,f,d,a,e)
                    else
                    if d < e then
                        writeln(c,b,f,d,e,a)
                    else
                    if f < e then
                        writeln(c,b,f,e,d,a)
                    else
                    if b < e then
                        writeln(c,b,e,f,d,a)
                    else
                    if c < e then
                        writeln(c,e,b,f,d,a)
                    else
                        writeln(e,c,b,f,d,a)
            else
                if a < e then
                    if e < c then
                        writeln(f,b,d,a,e,c)
                    else
                    if a < c then
                        writeln(f,b,d,a,c,e)
                    else
                    if d < c then
                        writeln(f,b,d,c,a,e)
                    else
                    if b < c then
                        writeln(f,b,c,d,a,e)
                    else
                    if f < c then
                        writeln(f,c,b,d,a,e)
                    else
                        writeln(c,f,b,d,a,e)
                else
                if d < e then
                    if a < c then
                        writeln(f,b,d,e,a,c)
                    else
                    if e < c then
                        writeln(f,b,d,e,c,a)
                    else
                    if d < c then
                        writeln(f,b,d,c,e,a)
                    else
                    if b < c then
                        writeln(f,b,c,d,e,a)
                    else
                    if f < c then
                        writeln(f,c,b,d,e,a)
                    else
                        writeln(c,f,b,d,e,a)
                else
                if b < e then
                    if a < c then
                        writeln(f,b,e,d,a,c)
                    else
                    if d < c then
                        writeln(f,b,e,d,c,a)
                    else
                    if e < c then
                        writeln(f,b,e,c,d,a)
                    else
                    if b < c then
                        writeln(f,b,c,e,d,a)
                    else
                    if f < c then
                        writeln(f,c,b,e,d,a)
                    else
                        writeln(c,f,b,e,d,a)
                else
                if f < e then
                    if a < c then
                        writeln(f,e,b,d,a,c)
                    else
                    if d < c then
                        writeln(f,e,b,d,c,a)
                    else
                    if b < c then
                        writeln(f,e,b,c,d,a)
                    else
                    if e < c then
                        writeln(f,e,c,b,d,a)
                    else
                    if f < c then
                        writeln(f,c,e,b,d,a)
                    else
                        writeln(c,f,e,b,d,a)
                else
                    if a < c then
                        writeln(e,f,b,d,a,c)
                    else
                    if d < c then
                        writeln(e,f,b,d,c,a)
                    else
                    if b < c then
                        writeln(e,f,b,c,d,a)
                    else
                    if f < c then
                        writeln(e,f,c,b,d,a)
                    else
                    if e < c then
                        writeln(e,c,f,b,d,a)
                    else
                        writeln(c,e,f,b,d,a)
        else
            if a < c then
                if c < e then
                    if e < f then
                        writeln(d,b,a,c,e,f)
                    else
                    if c < f then
                        writeln(d,b,a,c,f,e)
                    else
                    if a < f then
                        writeln(d,b,a,f,c,e)
                    else
                    if b < f then
                        writeln(d,b,f,a,c,e)
                    else
                    if d < f then
                        writeln(d,f,b,a,c,e)
                    else
                        writeln(f,d,b,a,c,e)
                else
                if a < e then
                    if c < f then
                        writeln(d,b,a,e,c,f)
                    else
                    if e < f then
                        writeln(d,b,a,e,f,c)
                    else
                    if a < f then
                        writeln(d,b,a,f,e,c)
                    else
                    if b < f then
                        writeln(d,b,f,a,e,c)
                    else
                    if d < f then
                        writeln(d,f,b,a,e,c)
                    else
                        writeln(f,d,b,a,e,c)
                else
                if b < e then
                    if c < f then
                        writeln(d,b,e,a,c,f)
                    else
                    if a < f then
                        writeln(d,b,e,a,f,c)
                    else
                    if e < f then
                        writeln(d,b,e,f,a,c)
                    else
                    if b < f then
                        writeln(d,b,f,e,a,c)
                    else
                    if d < f then
                        writeln(d,f,b,e,a,c)
                    else
                        writeln(f,d,b,e,a,c)
                else
                if d < e then
                    if c < f then
                        writeln(d,e,b,a,c,f)
                    else
                    if a < f then
                        writeln(d,e,b,a,f,c)
                    else
                    if b < f then
                        writeln(d,e,b,f,a,c)
                    else
                    if e < f then
                        writeln(d,e,f,b,a,c)
                    else
                    if d < f then
                        writeln(d,f,e,b,a,c)
                    else
                        writeln(f,d,e,b,a,c)
                else
                    if c < f then
                        writeln(e,d,b,a,c,f)
                    else
                    if a < f then
                        writeln(e,d,b,a,f,c)
                    else
                    if b < f then
                        writeln(e,d,b,f,a,c)
                    else
                    if d < f then
                        writeln(e,d,f,b,a,c)
                    else
                    if e < f then
                        writeln(e,f,d,b,a,c)
                    else
                        writeln(f,e,d,b,a,c)
            else
            if b < c then
                if a < f then
                    if f < e then
                        writeln(d,b,c,a,f,e)
                    else
                    if a < e then
                        writeln(d,b,c,a,e,f)
                    else
                    if c < e then
                        writeln(d,b,c,e,a,f)
                    else
                    if b < e then
                        writeln(d,b,e,c,a,f)
                    else
                    if d < e then
                        writeln(d,e,b,c,a,f)
                    else
                        writeln(e,d,b,c,a,f)
                else
                if c < f then
                    if a < e then
                        writeln(d,b,c,f,a,e)
                    else
                    if f < e then
                        writeln(d,b,c,f,e,a)
                    else
                    if c < e then
                        writeln(d,b,c,e,f,a)
                    else
                    if b < e then
                        writeln(d,b,e,c,f,a)
                    else
                    if d < e then
                        writeln(d,e,b,c,f,a)
                    else
                        writeln(e,d,b,c,f,a)
                else
                if b < f then
                    if a < e then
                        writeln(d,b,f,c,a,e)
                    else
                    if c < e then
                        writeln(d,b,f,c,e,a)
                    else
                    if f < e then
                        writeln(d,b,f,e,c,a)
                    else
                    if b < e then
                        writeln(d,b,e,f,c,a)
                    else
                    if d < e then
                        writeln(d,e,b,f,c,a)
                    else
                        writeln(e,d,b,f,c,a)
                else
                if d < f then
                    if a < e then
                        writeln(d,f,b,c,a,e)
                    else
                    if c < e then
                        writeln(d,f,b,c,e,a)
                    else
                    if b < e then
                        writeln(d,f,b,e,c,a)
                    else
                    if f < e then
                        writeln(d,f,e,b,c,a)
                    else
                    if d < e then
                        writeln(d,e,f,b,c,a)
                    else
                        writeln(e,d,f,b,c,a)
                else
                    if a < e then
                        writeln(f,d,b,c,a,e)
                    else
                    if c < e then
                        writeln(f,d,b,c,e,a)
                    else
                    if b < e then
                        writeln(f,d,b,e,c,a)
                    else
                    if d < e then
                        writeln(f,d,e,b,c,a)
                    else
                    if f < e then
                        writeln(f,e,d,b,c,a)
                    else
                        writeln(e,f,d,b,c,a)
            else
            if d < c then
                if a < e then
                    if e < f then
                        writeln(d,c,b,a,e,f)
                    else
                    if a < f then
                        writeln(d,c,b,a,f,e)
                    else
                    if b < f then
                        writeln(d,c,b,f,a,e)
                    else
                    if c < f then
                        writeln(d,c,f,b,a,e)
                    else
                    if d < f then
                        writeln(d,f,c,b,a,e)
                    else
                        writeln(f,d,c,b,a,e)
                else
                if b < e then
                    if a < f then
                        writeln(d,c,b,e,a,f)
                    else
                    if e < f then
                        writeln(d,c,b,e,f,a)
                    else
                    if b < f then
                        writeln(d,c,b,f,e,a)
                    else
                    if c < f then
                        writeln(d,c,f,b,e,a)
                    else
                    if d < f then
                        writeln(d,f,c,b,e,a)
                    else
                        writeln(f,d,c,b,e,a)
                else
                if c < e then
                    if a < f then
                        writeln(d,c,e,b,a,f)
                    else
                    if b < f then
                        writeln(d,c,e,b,f,a)
                    else
                    if e < f then
                        writeln(d,c,e,f,b,a)
                    else
                    if c < f then
                        writeln(d,c,f,e,b,a)
                    else
                    if d < f then
                        writeln(d,f,c,e,b,a)
                    else
                        writeln(f,d,c,e,b,a)
                else
                if d < e then
                    if a < f then
                        writeln(d,e,c,b,a,f)
                    else
                    if b < f then
                        writeln(d,e,c,b,f,a)
                    else
                    if c < f then
                        writeln(d,e,c,f,b,a)
                    else
                    if e < f then
                        writeln(d,e,f,c,b,a)
                    else
                    if d < f then
                        writeln(d,f,e,c,b,a)
                    else
                        writeln(f,d,e,c,b,a)
                else
                    if a < f then
                        writeln(e,d,c,b,a,f)
                    else
                    if b < f then
                        writeln(e,d,c,b,f,a)
                    else
                    if c < f then
                        writeln(e,d,c,f,b,a)
                    else
                    if d < f then
                        writeln(e,d,f,c,b,a)
                    else
                    if e < f then
                        writeln(e,f,d,c,b,a)
                    else
                        writeln(f,e,d,c,b,a)
            else
                if a < f then
                    if f < e then
                        writeln(c,d,b,a,f,e)
                    else
                    if a < e then
                        writeln(c,d,b,a,e,f)
                    else
                    if b < e then
                        writeln(c,d,b,e,a,f)
                    else
                    if d < e then
                        writeln(c,d,e,b,a,f)
                    else
                    if c < e then
                        writeln(c,e,d,b,a,f)
                    else
                        writeln(e,c,d,b,a,f)
                else
                if b < f then
                    if a < e then
                        writeln(c,d,b,f,a,e)
                    else
                    if f < e then
                        writeln(c,d,b,f,e,a)
                    else
                    if b < e then
                        writeln(c,d,b,e,f,a)
                    else
                    if d < e then
                        writeln(c,d,e,b,f,a)
                    else
                    if c < e then
                        writeln(c,e,d,b,f,a)
                    else
                        writeln(e,c,d,b,f,a)
                else
                if d < f then
                    if a < e then
                        writeln(c,d,f,b,a,e)
                    else
                    if b < e then
                        writeln(c,d,f,b,e,a)
                    else
                    if f < e then
                        writeln(c,d,f,e,b,a)
                    else
                    if d < e then
                        writeln(c,d,e,f,b,a)
                    else
                    if c < e then
                        writeln(c,e,d,f,b,a)
                    else
                        writeln(e,c,d,f,b,a)
                else
                if c < f then
                    if a < e then
                        writeln(c,f,d,b,a,e)
                    else
                    if b < e then
                        writeln(c,f,d,b,e,a)
                    else
                    if d < e then
                        writeln(c,f,d,e,b,a)
                    else
                    if f < e then
                        writeln(c,f,e,d,b,a)
                    else
                    if c < e then
                        writeln(c,e,f,d,b,a)
                    else
                        writeln(e,c,f,d,b,a)
                else
                    if a < e then
                        writeln(f,c,d,b,a,e)
                    else
                    if b < e then
                        writeln(f,c,d,b,e,a)
                    else
                    if d < e then
                        writeln(f,c,d,e,b,a)
                    else
                    if c < e then
                        writeln(f,c,e,d,b,a)
                    else
                    if f < e then
                        writeln(f,e,c,d,b,a)
                    else
                        writeln(e,f,c,d,b,a)
end.
