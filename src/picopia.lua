t_empty=0
t_grass=1
t_dry_grass=2
t_tall_grass=3
t_dry_tall_grass=4
t_bush=5
t_dry_bush=6
t_tree=7
t_dry_tree=8
t_soil=9
t_dry_soil=10
t_flower=11
t_dry_flower=12
t_stone=13

grid={}
world_w=32
world_h=32

helpers={
 {name="watbit",c=12,icon=21,used=false},
 {name="sproutbit",c=11,icon=22,used=false},
 {name="chopbit",c=10,icon=19,used=false},
 {name="smashbit",c=6,icon=20,used=false}
}

function _init()
 for y=1,world_h do
  grid[y]={}
  for x=1,world_w do
   grid[y][x]=mget(x-1,y-1)
  end
 end
 player={x=16,y=16,dx=0,dy=1,walk=0}
 active=1
 msg="restore picopia"
 msg_t=90
 fx={}
 complete=false
 goal=1
 quest=true
 help=true
 tw=0
end

function _update()
 tw+=1
 update_fx()
 if help then
  if btnp(4) or btnp(5) then help=false sfx(4) end
  return
 end
 if quest then
  if btnp(4) or btnp(5) then quest=false sfx(4) end
  return
 end
 if quest_shortcut() then
  quest=true
  sfx(4)
  return
 end
 if btnp(4) then cycle_helper(1) end
 move_input()
 if btnp(5) then act() end
 check_done()
end

function quest_shortcut()
 return (btn(4) and btnp(5)) or (btn(5) and btnp(4))
end

function move_input()
 local nx=player.x
 local ny=player.y
 local dx=0
 local dy=0
 if btnp(0) then dx=-1 end
 if btnp(1) then dx=1 end
 if btnp(2) then dy=-1 end
 if btnp(3) then dy=1 end
 if dx!=0 and dy!=0 then dy=0 end
 if dx!=0 or dy!=0 then
  nx+=dx
  ny+=dy
  player.dx=dx
  player.dy=dy
  if can_walk(nx,ny) then
   player.x=nx
   player.y=ny
   player.walk=6
  else
   say("blocked",20)
  end
 end
 if player.walk>0 then player.walk-=1 end
end

function can_walk(x,y)
 if x<1 or x>world_w or y<1 or y>world_h then return false end
 local t=grid[y][x]
 return t!=t_bush and t!=t_dry_bush and t!=t_tree and t!=t_dry_tree and t!=t_stone
end

function cycle_helper(d)
 active+=d
 if active<1 then active=#helpers end
 if active>#helpers then active=1 end
 say(helpers[active].name,35)
 sfx(0)
 add_fx(player.x,player.y,helpers[active].c,"swap")
end

function act()
 if use_helper() then return end
 nope()
end

function use_helper()
 local tx=player.x+player.dx
 local ty=player.y+player.dy
 if tx<1 or tx>world_w or ty<1 or ty>world_h then return false end
 local h=helpers[active]
 local t=grid[ty][tx]
 local dst=tool_dst(h.name,t)
 if dst!=nil then
  grid[ty][tx]=dst
  h.used=true
  sfx(1)
  add_fx(tx,ty,h.c,h.name)
  say(h.name.."!",25)
  return true
 end
 return false
end

function tool_dst(name,t)
 if name=="watbit" then
  if t==t_dry_grass then return t_grass end
  if t==t_dry_tall_grass then return t_tall_grass end
  if t==t_dry_bush then return t_bush end
  if t==t_dry_tree then return t_tree end
  if t==t_dry_soil then return t_soil end
  if t==t_dry_flower then return t_flower end
 elseif name=="sproutbit" then
  if t==t_grass then return t_tall_grass end
 elseif name=="chopbit" then
  if t==t_tall_grass or t==t_bush or t==t_tree then return t_grass end
  if t==t_dry_tall_grass or t==t_dry_bush or t==t_dry_tree then return t_grass end
 elseif name=="smashbit" then
  if t==t_stone then return t_soil end
 end
 return nil
end

function nope()
 say("nope",20)
 sfx(2)
 add_fx(player.x+player.dx,player.y+player.dy,5,"nope")
end

function add_fx(x,y,c,kind)
 add(fx,{x=x*8-4,y=y*8-4,c=c,t=18,k=kind})
end

function update_fx()
 for i=#fx,1,-1 do
  local f=fx[i]
  f.t-=1
  f.y-=0.2
  if f.t<=0 then deli(fx,i) end
 end
 if msg_t>0 then msg_t-=1 end
end

function say(s,t)
 msg=s
 msg_t=t
end

function used_count()
 local n=0
 for h in all(helpers) do
  if h.used then n+=1 end
 end
 return n
end

function check_done()
 if not complete and used_count()>=#helpers then
  complete=true
  goal=2
  quest=true
  say("all tools used",160)
  sfx(3)
  for i=1,24 do
   add_fx(rnd(16)+1,rnd(12)+2,7+flr(rnd(5)),"spark")
  end
 end
end

function _draw()
 cls(1)
 local cx=mid(0,player.x*8-64,world_w*8-128)
 local cy=mid(0,player.y*8-64,world_h*8-128)
 camera(cx,cy)
 draw_world()
 draw_sproutroot()
 draw_player()
 draw_fx()
 camera()
 draw_hud()
 if quest then draw_quest() end
 if help then draw_help() end
end

function draw_world()
 for y=1,world_h do
  for x=1,world_w do
   draw_tile(x,y,grid[y][x])
  end
 end
end

function draw_tile(x,y,t)
 spr(t,(x-1)*8,(y-1)*8)
end

function draw_player()
 local px=(player.x-1)*8
 local py=(player.y-1)*8
 local bob=0
 if player.walk>0 then bob=player.walk%2 end
 spr(16+player.walk%2,px,py-bob)
 local tx=px+4+player.dx*4
 local ty=py+4+player.dy*4
 pset(tx,ty,7)
end

function draw_sproutroot()
 spr(18,13*8,8)
end

function draw_fx()
 for f in all(fx) do
  local a=f.t/18
  circfill(f.x,f.y,1+a*2,f.c)
  if f.k=="watbit" then
   line(f.x,f.y-3,f.x,f.y+3,12)
  elseif f.k=="chopbit" then
   line(f.x-3,f.y+3,f.x+3,f.y-3,7)
  elseif f.k=="sproutbit" then
   pset(f.x,f.y-3,11)
   pset(f.x-2,f.y,11)
   pset(f.x+2,f.y,11)
  elseif f.k=="smashbit" then
   circ(f.x,f.y,3,6)
  end
 end
end

function draw_hud()
 rectfill(0,112,127,127,0)
 print("picopia",2,114,7)
 local h=helpers[active]
 spr(h.icon,34,114)
 print(h.name,44,114,h.c)
 print("tools:"..used_count().."/"..#helpers,2,122,6)
 if msg_t>0 then print(msg,56,122,7) end
end

function draw_quest()
 rectfill(14,28,113,92,0)
 rect(14,28,113,92,7)
 print("quest",52,34,11)
 if goal==1 then
  print("use four tools",22,48,7)
  print("tools:"..used_count().."/"..#helpers,22,58,11)
  print("restore and clear",22,68,10)
 else
  print("free play",22,48,14)
  print("all tools tested",22,60,11)
  print("keep restoring",22,72,7)
 end
 print("press o/x",40,84,6)
end

function draw_help()
 rectfill(8,12,119,108,0)
 rect(8,12,119,108,7)
 draw_logo()
 print("restore a tiny world",22,40,6)
 line(20,50,108,50,5)
 print("arrows  move",24,58,7)
 print("o       next tool",24,68,10)
 print("x       use tool",24,78,12)
 print("o+x     quest",24,88,14)
 print("press o or x",36,102,6)
end

function draw_logo()
 spr(t_flower,36,18)
 print("PICOPIA",51,20,5)
 print("PICOPIA",50,19,11)
 spr(t_dry_grass,88,18)
 pset(32,18,7)
 pset(99,21,7)
 pset(40,31,10)
 pset(91,31,10)
end
