# Test Strategy: Detail Modal Transition

## 1. Risk Assessment
- **Medium Risk**: Modal might not trigger reliably on map click.
- **Low Risk**: Chart rendering issues inside the modal.
- **Low Risk**: Mobile responsiveness of the large modal.

## 2. Test Plan

### A. Manual Verification (Critical)
1. **Trigger Check**: Start app -> click a marker -> click "View Details".
   - **Expectation**: Modal appears immediately.
2. **Content Check**: Verify Name, Island, Type, HA, Aide, Mayor are correct.
3. **Analytics Check**: Verify Trend Chart and Historical Table render fully within the "large" modal.
4. **Dismissal Check**: Click "X", click backdrop, press ESC, click "Close Details".
   - **Expectation**: Modal closes and returns to the map view.
5. **Direct Navigation**: Navigate to `/?selected_center=NAMET_HEALTH_CENTRE`.
   - **Expectation**: App loads with the modal already open for that center.

### B. Automated Coverage
- **Linting**: Ensure `flake8` and `black` pass on `detail_modal.py` and `main.py`.

## 3. Quality Gates
| Gate | Criteria |
|------|----------|
| Visual Check | 5/5 manual tests pass |
| Linting | Zero errors in new/modified files |
| State Management | `detail_center` correctly cleared on close |
