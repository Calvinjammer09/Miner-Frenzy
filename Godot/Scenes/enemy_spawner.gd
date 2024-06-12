extends Node2D

@export var enemy_scene : PackedScene

@onready var game = get_node('/root/Game')

var spawn_points := []
var wave = 0

func _ready():
	for i in get_children():
		if i is Marker2D:
			spawn_points.append(i)

func _on_spawn_timer_timeout():
	var enemy = enemy_scene.instantiate()
	var spawn = spawn_points[randi() % spawn_points.size()]
	
	print(spawn.position)

	enemy.position = spawn.position
	enemy.name = 'Enemy'

	add_child(enemy)
	
	enemy.add_to_group('enemies')
	
	wave += 1
	
	if wave >= 7 and wave <= 12:
		$SpawnTimer.wait_time -= 0.1
	elif wave == 20:
		$SpawnTimer.wait_time -= 0.1

func _process(_delta):
	for spawn in spawn_points:
		spawn.position.x = $"../Player".position.x + (get_viewport_rect().size.x / 2) - spawn.position.x
		spawn.position.y = $"../Player".position.y + (get_viewport_rect().size.y / 2) - spawn.position.y
	
	
