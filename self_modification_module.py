import os
import difflib
import logging
from datetime import datetime

class SelfModificationModule:
    """
    Safely allows the AI to propose and execute self-edits under strict criteria.
    All changes are logged and require justification, tests, and a rollback snapshot.
    """
    def __init__(self, project_root, log_path="self_modification.log", snapshot_dir=".self_mod_snapshots"):
        self.project_root = project_root
        self.log_path = os.path.join(project_root, log_path)
        self.snapshot_dir = os.path.join(project_root, snapshot_dir)
        os.makedirs(self.snapshot_dir, exist_ok=True)
        logging.basicConfig(filename=self.log_path, level=logging.INFO)

    def _snapshot(self, target_file):
        """Save a timestamped backup of the file before mutation."""
        ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
        base = os.path.basename(target_file)
        snap_path = os.path.join(self.snapshot_dir, f"{base}.{ts}.bak")
        with open(target_file, "rb") as f_in, open(snap_path, "wb") as f_out:
            f_out.write(f_in.read())
        return snap_path

    def _log_change(self, target_file, justification, diff):
        with open(self.log_path, "a", encoding="utf-8") as log:
            log.write(f"\n[{datetime.utcnow().isoformat()}] {target_file}\nJustification: {justification}\nDiff:\n{diff}\n{'-'*40}\n")

    def _generate_diff(self, old_content, new_content):
        return ''.join(difflib.unified_diff(
            old_content.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            fromfile='original',
            tofile='modified'))

    def criteria_met(self, justification, tests_passed, impact_level):
        """
        Strict criteria for allowing self-edit:
        - Justification must be strong (e.g., critical bug, major improvement, or user-approved feature)
        - Automated or user-confirmed tests must pass
        - Impact level must be 'safe', 'minor', or explicitly user-approved
        """
        if not justification or len(justification) < 15:
            return False
        if not tests_passed:
            return False
        if impact_level not in ("safe", "minor", "user-approved"):
            return False
        return True

    def propose_and_apply_edit(self, target_file, new_content, justification, tests_passed, impact_level="safe"):
        """
        Propose and, if criteria are met, apply a code edit to the target file.
        Returns True if applied, False otherwise.
        """
        if not os.path.isfile(target_file):
            raise FileNotFoundError(f"Target file not found: {target_file}")
        with open(target_file, "r", encoding="utf-8") as f:
            old_content = f.read()
        if old_content == new_content:
            return False  # No change needed
        if not self.criteria_met(justification, tests_passed, impact_level):
            return False
        snap_path = self._snapshot(target_file)
        diff = self._generate_diff(old_content, new_content)
        self._log_change(target_file, justification, diff)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        logging.info(f"[SelfModification] {target_file} edited. Snapshot: {snap_path}")
        return True

    def rollback_last(self, target_file):
        """
        Restore the most recent snapshot for the target file.
        """
        base = os.path.basename(target_file)
        snaps = [f for f in os.listdir(self.snapshot_dir) if f.startswith(base) and f.endswith(".bak")]
        if not snaps:
            raise FileNotFoundError("No snapshots found for rollback.")
        snaps.sort(reverse=True)
        snap_path = os.path.join(self.snapshot_dir, snaps[0])
        with open(snap_path, "rb") as f_in, open(target_file, "wb") as f_out:
            f_out.write(f_in.read())
        logging.info(f"[SelfModification] {target_file} rolled back to snapshot {snap_path}")
        return snap_path
