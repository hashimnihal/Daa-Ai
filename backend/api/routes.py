# backend/api/routes.py

from fastapi import APIRouter

router = APIRouter()


# Dijkstra Route
@router.get("/dijkstra")
def run_dijkstra():

    # Add Dijkstra Function Here Later

    pass


# A* Route
@router.get("/astar")
def run_astar():

    # Add A* Function Here Later

    pass


# Greedy Route
@router.get("/greedy")
def run_greedy():

    # Add Greedy Function Here Later

    pass