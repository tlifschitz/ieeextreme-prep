**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/rumors/>

# Rumors

**IEEEXtreme 17.0** · Time limit: 2000 ms · Memory limit: 256 MB

A rumor has been spreading about the much-anticipated next generation phone from Xtreme Tech, Inc.  To determine whether the rumor is credible, we would like to know the possible sources of the rumor.

We have assembled a list of all of the pairs of people who have been involved in spreading the rumor.  For some pairs, we know who said the rumor and who heard it; for example, we might know that Bob heard the rumor for the first time from Alice.  However, for others, we just know that two people were involved in spreading the rumor; for example, we just know that either Chuck heard the rumor for the first time from Dev or that Dev heard the rumor for the first time from Chuck.

## Standard Input

Input begins with an integer $n$ on a line by itself.

The next $n$ lines take one of two forms.

If we know that person `p2` heard the rumor for the first time from person `p1`, the line will appear as:

	`p1 -> p2`

If we know that either `p2` heard the rumor for the first time from `p1` or that `p1` heard the rumor for the first time from `p2`, the line will have the form:

	`p1 ?? p2`

## Standard Output

Output the possible source of the rumors, given the relationships described in the input.  If there is more than one possible source, output the sources, one per line, in alphabetical order.

## Constraints and notes

- $1 \leq n \leq 10^5$

No two people will have the same name.

The people's names will consist of lowercase letters, with a length between 1 and 5 characters.

Since we record only the first time a person hears a rumor, a person cannot hear the rumor from multiple sources.

## Examples

### Example 1

Input:
```
4
alice ?? bob
bob -> chuck
bob -> dev
dev ?? eve
```

Output:
```
alice
bob
```

Explanation:

We know that chuck and dev could not be the source of the rumor because both heard the rumor for the first time from bob.  We also know that eve must have heard the rumor from dev, because dev heard it from the first time from bob.  That leaves alice and bob as the possible sources, and we do not know if alice heard the rumor from bob, or vice versa.
