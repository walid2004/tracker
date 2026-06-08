export function resetTheState(session) {
  if (!session) {
    console.warn("Trying to reset the state.");
    return;
  }
  session.fallbackCount = 0;

}