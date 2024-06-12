extends Camera2D

var dead = false

func _process(_delta):
	if not dead:
		position += $"../Player".position - position
	else:
		position.x = 0
		position.y = 0
		
func _on_player_dead(_dead):
	dead = true
