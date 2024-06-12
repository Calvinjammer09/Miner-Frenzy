extends Node2D


var restart = false

func _on_player_dead(dead):
	$EndTimer.start()
	
	
	print(dead)
	if not dead:
		get_node('EndScreen').visible = true
	else:
		get_node('YouLost').visible = true
		
func _process(_delta):
	if restart:
		if Input:
			get_tree().change_scene_to_file("res://Scenes/menu.tscn")
			
func _on_end_timer_timeout():
	restart = true
