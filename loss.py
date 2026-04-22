import torch
import torch.nn.functional as F


def pose_loss_norm(pred, gt, eps=1e-6, lambda_t: float = 1.0, lambda_r: float = 1.0, reduction: str = 'mean'):
    gt_R = gt[:, :3]
    gt_T = gt[:, 3:]
    pred_R = pred[:, :3]
    pred_T = pred[:, 3:]

    # Compute norms
    norm_pred_T = torch.norm(pred_T, dim=1, keepdim=True).clamp(min=eps)
    norm_gt_T = torch.norm(gt_T, dim=1, keepdim=True).clamp(min=eps)

    # Normalize translations
    pred_T_unit = pred_T / norm_pred_T
    gt_T_unit = gt_T / norm_gt_T

    # Compute translation and rotation losses
    trans_loss = F.l1_loss(pred_T_unit, gt_T_unit, reduction=reduction)
    rot_loss = F.l1_loss(pred_R, gt_R, reduction=reduction)

    return lambda_t * trans_loss + lambda_r * rot_loss


def pose_error(gt, pred):
    """Compute the pose error between true and predicted poses."""
    return torch.mean(torch.linalg.norm(pred - gt, dim=1, ord=2))
