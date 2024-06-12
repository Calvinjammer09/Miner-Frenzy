extends Area2D

var speed = 50
var direction : Vector2
var damage = 3

func _ready():
	$DespawnTimer.start()

func _process(_delta):
	position += speed * direction

func _on_body_entered(body):
	body.health -= damage
	queue_free()

func _on_despawn_timer_timeout():
	queue_free()
