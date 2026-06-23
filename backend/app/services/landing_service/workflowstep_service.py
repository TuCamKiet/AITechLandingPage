from sqlalchemy.orm import Session

from app.models.landing_model.workflowstep_model import WorkflowStep


def get_all_workflow_steps(db: Session):
    return db.query(WorkflowStep).all()


def get_workflow_step_by_id(
    db: Session,
    workflow_step_id: int
):
    return (
        db.query(WorkflowStep)
        .filter(
            WorkflowStep.id == workflow_step_id
        )
        .first()
    )


def create_workflow_step(
    db: Session,
    workflow_step_data
):
    workflow_step = WorkflowStep(
        step=workflow_step_data.step,
        title=workflow_step_data.title,
        detail=workflow_step_data.detail
    )

    db.add(workflow_step)

    db.commit()
    db.refresh(workflow_step)

    return workflow_step


def update_workflow_step(
    db: Session,
    workflow_step_id: int,
    workflow_step_data
):
    workflow_step = get_workflow_step_by_id(
        db,
        workflow_step_id
    )

    if not workflow_step:
        return None

    workflow_step.step = workflow_step_data.step
    workflow_step.title = workflow_step_data.title
    workflow_step.detail = workflow_step_data.detail

    db.commit()
    db.refresh(workflow_step)

    return workflow_step


def delete_workflow_step(
    db: Session,
    workflow_step_id: int
):
    workflow_step = get_workflow_step_by_id(
        db,
        workflow_step_id
    )

    if not workflow_step:
        return False

    db.delete(workflow_step)

    db.commit()

    return True