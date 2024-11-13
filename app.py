from flask import Flask, jsonify, request

app = Flask(__name__)

ideas = {    # This line and everything after needs to be indented!
            "post_ideas": [
                {
                    "title": "Best Oklahoma Towns to Visit in December",
                    "keyword": "Best Places to Visit in December",
                    "kd": 3,
                    "volume": 1200
                },
                {
                    "title": "Where to See Christmas Lights in Tulsa",
                    "keyword": "Christmas Lights Near Me",
                    "kd": 4,
                    "volume": 34000
                },
                {
                    "title": "Christmas Events in Missouri",
                    "keyword": "Christmas Events Near Me",
                    "kd": 1,
                    "volume": 26000
                }
            ]
        }

@app.route('/api/blog-stats')
def get_blog_stats():
    stats = {
        "total_posts": 10,
        "top_performing_posts": [
            {
                "title": "Things to Do in a Small Town",
                "views": 1500,
                "category": "Road Trips"
            },
            {
                "title": "Road Trip Food Ideas - No Refrigeration Required",
                "views": 1200,
                "category": "Road Trips"
            },
            {
                "title": "Oklahoma Christmas Towns",
                "views": 1000,
                "category": "Small Town Travel Guides"
            }
        ],
        "monthly_visitors": 500,
        "trending_categories": ["Road Trips", "Small Town Travel Guides"],
        "top_states": ["Oklahoma", "Texas", "Kansas"]
    }
    return jsonify(stats)

@app.route('/api/va-tasks')
def get_va_tasks():
    tasks = {
        "pending_tasks": [
            {
                "id": 1,
                "title": "Research Small Towns in Texas Hill Country",
                "type": "research",
                "status": "pending",
                "due_date": "2024-01-15",
                "priority": "high"
            },
            {
                "id": 2,
                "title": "Optimize Images for Oklahoma Christmas Towns Post",
                "type": "image_optimization",
                "status": "pending",
                "due_date": "2024-01-20",
                "priority": "medium"
            },
            {
                "id": 3,
                "title": "Draft Road Trip Snacks for Summer Travel",
                "type": "content_writing",
                "status": "pending",
                "due_date": "2024-01-25",
                "priority": "medium"
            }
        ],
        "task_metrics": {
            "total_pending": 3,
            "by_type": {
                "research": 1,
                "image_optimization": 1,
                "content_writing": 1
            },
            "high_priority": 1
        }
    }
    return jsonify(tasks)

@app.route('/api/post-ideas', methods=["GET", "POST"]) # Test
def get_post_ideas():
    global ideas
    if request.method == "POST":
        # Get the new idea from the request
        new_idea = request.json

          # Add this variable to track if we found a duplicate
        is_duplicate = False
        
        # Check each existing idea
        for idea in ideas["post_ideas"]:
            if idea["title"] == new_idea["title"]:
                is_duplicate = True
                break  # Exit the loop if we found a match
        
        # Now AFTER the loop, decide what to do
        if is_duplicate:
            return jsonify({"message": "This idea already exists!"})
        else:
            ideas["post_ideas"].append(new_idea)
            return jsonify({"message": "New idea added successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)